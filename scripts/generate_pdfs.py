#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import functools
import http.server
import socket
import threading
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "assets" / "pdfs"

PDF_JOBS = [
    {
        "route": "resume",
        "variant": "국문 Resume",
        "output": "resume_kr.pdf",
        "wait_text": "정현식",
    },
    {
        "route": "resume",
        "variant": "English Resume",
        "output": "resume_en.pdf",
        "wait_text": "Hyunsik Jung",
    },
    {
        "route": "cv",
        "output": "cv_kr.pdf",
        "wait_text": "Professional Summary",
    },
    {
        "route": "projects",
        "output": "projects_kr.pdf",
        "wait_text": "Deep Case Studies",
    },
]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


def free_port() -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def object_length(value: object) -> int:
    if not value:
        return 0
    with contextlib.suppress(AttributeError):
        value = value.get_object()
    return len(value)  # type: ignore[arg-type]


def page_has_visible_content(page: object) -> bool:
    if (page.extract_text() or "").strip():
        return True

    resources = page.get("/Resources") or {}
    with contextlib.suppress(AttributeError):
        resources = resources.get_object()

    return object_length(resources.get("/XObject")) > 0


def trim_trailing_blank_pages(path: Path) -> None:
    reader = PdfReader(str(path))
    last_content_index = len(reader.pages) - 1
    while last_content_index >= 0 and not page_has_visible_content(reader.pages[last_content_index]):
        last_content_index -= 1

    if last_content_index == len(reader.pages) - 1:
        return

    writer = PdfWriter()
    for page in reader.pages[: last_content_index + 1]:
        writer.add_page(page)

    with path.open("wb") as output:
        writer.write(output)


def main() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", free_port()), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    base_url = f"http://127.0.0.1:{server.server_port}"
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 1600})
            for job in PDF_JOBS:
                page.emulate_media(media="screen")
                page.goto(f"{base_url}/#{job['route']}", wait_until="networkidle")
                page.wait_for_selector(".document", timeout=10_000)

                variant = job.get("variant")
                if variant:
                    page.get_by_role("tab", name=variant).click()
                    page.wait_for_timeout(250)
                    page.wait_for_function(
                        "text => document.body.innerText.includes(text)",
                        arg=job["wait_text"],
                        timeout=10_000,
                    )

                page.emulate_media(media="print")
                output_path = PDF_DIR / job["output"]
                page.pdf(
                    path=str(output_path),
                    format="A4",
                    print_background=True,
                    prefer_css_page_size=True,
                )
                trim_trailing_blank_pages(output_path)
                print(f"wrote {output_path.relative_to(ROOT)}")

            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_required(path: str) -> str:
    file_path = ROOT / path
    if not file_path.is_file():
        raise SystemExit(f"FAIL: missing {path}")
    return file_path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"FAIL: {label}")


def main() -> None:
    html = read_required("index.html")
    css = read_required("styles.css")
    js = read_required("app.js")

    require(html, '<link rel="stylesheet" href="styles.css">', "index must load styles.css")
    require(html, '<script src="app.js" defer></script>', "index must load app.js")
    require(html, 'id="sidebar"', "index must expose sidebar")
    require(html, 'id="content"', "index must expose content")
    require(css, ".layout", "styles must define layout")
    require(css, "@media (max-width: 760px)", "styles must include mobile behavior")
    require(css, "position: sticky", "sidebar must stay visible on desktop")
    require(js, 'fetch("data/site.json"', "renderer must load manifest")
    require(js, "location.hash", "renderer must support hash navigation")
    require(js, 'document.createElement("video")', "renderer must render videos")
    require(js, 'document.createElement("img")', "renderer must render images")
    require(js, "markdownSrc", "renderer must render markdown documents")
    require(js, "variants", "renderer must support document variants")
    require(js, "mediaGroups", "renderer must render grouped media")
    require(js, "renderProfile", "renderer must render profile headers")
    require(css, ".profile-meta", "styles must align profile metadata")
    require(css, ".variant-controls", "styles must define document variant controls")

    if not (ROOT / ".nojekyll").is_file():
        raise SystemExit("FAIL: missing .nojekyll")

    print("shell ok")


if __name__ == "__main__":
    main()

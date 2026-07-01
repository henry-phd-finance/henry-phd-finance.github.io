#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "site.json"

EXPECTED = {
    "jaeyong-conversation": {
        "label": "이재용 부회장과의 대화",
        "media": [
            ("image", "assets/jaeyong-conversation/body_image_1.png"),
            ("image", "assets/jaeyong-conversation/body_image_2.png"),
            ("image", "assets/jaeyong-conversation/body_image_3.png"),
            ("video", "assets/jaeyong-conversation/attached_video_1.mp4"),
            ("video", "assets/jaeyong-conversation/attached_video_2.mp4"),
            ("image", "assets/jaeyong-conversation/comments_full.png"),
        ],
    },
    "study-room": {
        "label": "어둠의 공부방 소개",
        "media": [
            ("image", "assets/study-room/body_image_1.png"),
            ("image", "assets/study-room/body_image_2.png"),
            ("video", "assets/study-room/attached_video.mp4"),
            ("image", "assets/study-room/comments_full.png"),
        ],
    },
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    if not MANIFEST.exists():
        fail("missing data/site.json")

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("siteLabel") != "Archive":
        fail("siteLabel must be Archive")

    sections = data.get("sections")
    if not isinstance(sections, list):
        fail("sections must be a list")

    slugs = [section.get("slug") for section in sections]
    if slugs != list(EXPECTED.keys()):
        fail(f"unexpected section order: {slugs}")

    for section in sections:
        slug = section["slug"]
        expected = EXPECTED[slug]
        if section.get("label") != expected["label"]:
            fail(f"{slug} label mismatch")

        media = section.get("media")
        if not isinstance(media, list):
            fail(f"{slug} media must be a list")

        actual = [(item.get("type"), item.get("src")) for item in media]
        if actual != expected["media"]:
            fail(f"{slug} media mapping mismatch: {actual}")

        for item_type, src in actual:
            if item_type not in {"image", "video"}:
                fail(f"{src} has invalid media type {item_type}")
            if not (ROOT / src).is_file():
                fail(f"{src} does not exist")

    print("manifest ok")


if __name__ == "__main__":
    main()

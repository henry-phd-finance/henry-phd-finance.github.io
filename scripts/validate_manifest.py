#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "site.json"

REQUIRED_SECTIONS = {
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

    seen_slugs: set[str] = set()
    by_slug: dict[str, dict] = {}
    for section in sections:
        if not isinstance(section, dict):
            fail("each section must be an object")

        slug = section.get("slug")
        if not isinstance(slug, str) or not slug.strip():
            fail("section slug must be a non-empty string")
        if slug in seen_slugs:
            fail(f"duplicate section slug: {slug}")
        seen_slugs.add(slug)
        by_slug[slug] = section

        label = section.get("label")
        if not isinstance(label, str) or not label.strip():
            fail(f"{slug} label must be a non-empty string")

        media = section.get("media")
        if not isinstance(media, list):
            fail(f"{slug} media must be a list")

        actual = [(item.get("type"), item.get("src")) for item in media]
        for item in media:
            if not isinstance(item, dict):
                fail(f"{slug} media item must be an object")
            item_type = item.get("type")
            src = item.get("src")
            alt = item.get("alt")
            if item_type not in {"image", "video"}:
                fail(f"{src} has invalid media type {item_type}")
            if not isinstance(src, str) or not src.strip():
                fail(f"{slug} media item must have a non-empty src")
            if not isinstance(alt, str) or not alt.strip():
                fail(f"{src} must have non-empty alt text")
            if not (ROOT / src).is_file():
                fail(f"{src} does not exist")

        if slug in REQUIRED_SECTIONS:
            expected = REQUIRED_SECTIONS[slug]
            if label != expected["label"]:
                fail(f"{slug} label mismatch")
            missing = [pair for pair in expected["media"] if pair not in actual]
            if missing:
                fail(f"{slug} missing required media: {missing}")

    missing_sections = [slug for slug in REQUIRED_SECTIONS if slug not in by_slug]
    if missing_sections:
        fail(f"missing required sections: {missing_sections}")

    print("manifest ok")


if __name__ == "__main__":
    main()

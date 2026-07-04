#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "site.json"

EXPECTED_ORDER = [
    "resume",
    "cv",
    "projects",
    "recognition",
    "research",
    "about",
    "contact",
]

REQUIRED_MEDIA = {
    "recognition": [
        ("image", "assets/jaeyong-conversation/body_image_1.png"),
        ("image", "assets/jaeyong-conversation/body_image_2.png"),
        ("image", "assets/jaeyong-conversation/body_image_3.png"),
        ("video", "assets/jaeyong-conversation/attached_video_1.mp4"),
        ("video", "assets/jaeyong-conversation/attached_video_2.mp4"),
        ("image", "assets/jaeyong-conversation/comments_full.png"),
        ("image", "assets/study-room/body_image_1.png"),
        ("image", "assets/study-room/body_image_2.png"),
        ("video", "assets/study-room/attached_video.mp4"),
        ("image", "assets/study-room/comments_full.png"),
    ],
}

REQUIRED_DOCUMENTS = {
    "resume": [
        "assets/documents/resume_kr.md",
        "assets/documents/resume_en.md",
    ],
    "cv": [
        "assets/documents/cv_kr.md",
    ],
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def validate_markdown_path(slug: str, markdown_src: object) -> None:
    if not isinstance(markdown_src, str) or not markdown_src.strip():
        fail(f"{slug} markdownSrc must be a non-empty string")
    if not (ROOT / markdown_src).is_file():
        fail(f"{markdown_src} does not exist")


def validate_profile(slug: str, profile: object) -> None:
    if not isinstance(profile, dict):
        fail(f"{slug} profile must be an object")
    if not isinstance(profile.get("name"), str) or not profile["name"].strip():
        fail(f"{slug} profile name must be a non-empty string")
    if not isinstance(profile.get("headline"), str) or not profile["headline"].strip():
        fail(f"{slug} profile headline must be a non-empty string")
    contacts = profile.get("contacts")
    if not isinstance(contacts, list) or not contacts:
        fail(f"{slug} profile contacts must be a non-empty list")
    for contact in contacts:
        if not isinstance(contact, dict):
            fail(f"{slug} profile contact must be an object")
        if not isinstance(contact.get("label"), str) or not contact["label"].strip():
            fail(f"{slug} profile contact label must be a non-empty string")
        if not isinstance(contact.get("value"), str) or not contact["value"].strip():
            fail(f"{slug} profile contact value must be a non-empty string")


def document_sources(section: dict) -> list[str]:
    sources = []
    if isinstance(section.get("markdownSrc"), str):
        sources.append(section["markdownSrc"])
    for variant in section.get("variants", []):
        if isinstance(variant, dict) and isinstance(variant.get("markdownSrc"), str):
            sources.append(variant["markdownSrc"])
    return sources


def main() -> None:
    if not MANIFEST.exists():
        fail("missing data/site.json")

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("siteLabel") != "Hyunsik Jung":
        fail("siteLabel must be Hyunsik Jung")

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

        media_items = []
        media = section.get("media", [])
        if not isinstance(media, list):
            fail(f"{slug} media must be a list")
        media_items.extend(media)

        media_groups = section.get("mediaGroups", [])
        if not isinstance(media_groups, list):
            fail(f"{slug} mediaGroups must be a list")
        for group in media_groups:
            if not isinstance(group, dict):
                fail(f"{slug} media group must be an object")
            if not isinstance(group.get("title"), str) or not group["title"].strip():
                fail(f"{slug} media group title must be a non-empty string")
            group_media = group.get("media")
            if not isinstance(group_media, list):
                fail(f"{slug} media group must include media list")
            media_items.extend(group_media)

        actual = [(item.get("type"), item.get("src")) for item in media_items]
        for item in media_items:
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

        markdown_src = section.get("markdownSrc")
        if markdown_src is not None:
            validate_markdown_path(slug, markdown_src)

        variants = section.get("variants", [])
        if not isinstance(variants, list):
            fail(f"{slug} variants must be a list")
        for variant in variants:
            if not isinstance(variant, dict):
                fail(f"{slug} variant must be an object")
            if not isinstance(variant.get("label"), str) or not variant["label"].strip():
                fail(f"{slug} variant label must be a non-empty string")
            validate_markdown_path(slug, variant.get("markdownSrc"))
            if "profile" in variant:
                validate_profile(slug, variant["profile"])

        if "profile" in section:
            validate_profile(slug, section["profile"])

        if slug in REQUIRED_MEDIA:
            missing = [pair for pair in REQUIRED_MEDIA[slug] if pair not in actual]
            if missing:
                fail(f"{slug} missing required media: {missing}")

    order = [section["slug"] for section in sections]
    if order != EXPECTED_ORDER:
        fail(f"section order mismatch: {order}")

    missing_sections = [slug for slug in EXPECTED_ORDER if slug not in by_slug]
    if missing_sections:
        fail(f"missing required sections: {missing_sections}")

    for slug, documents in REQUIRED_DOCUMENTS.items():
        actual_documents = document_sources(by_slug[slug])
        missing_documents = [document for document in documents if document not in actual_documents]
        if missing_documents:
            fail(f"{slug} missing required documents: {missing_documents}")

    print("manifest ok")


if __name__ == "__main__":
    main()

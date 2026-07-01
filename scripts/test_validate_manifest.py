#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("validate_manifest.py")
ROOT = SCRIPT.parents[1]


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_manifest", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load validate_manifest.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = load_validator()
        self.data = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))

    def run_validator_with(self, data: dict) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest = Path(tmpdir) / "site.json"
            manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            original_manifest = self.validator.MANIFEST
            self.validator.MANIFEST = manifest
            try:
                self.validator.main()
            finally:
                self.validator.MANIFEST = original_manifest

    def test_current_manifest_passes(self) -> None:
        self.run_validator_with(self.data)

    def test_valid_extra_section_passes(self) -> None:
        data = copy.deepcopy(self.data)
        data["sections"].append(
            {
                "slug": "resume",
                "label": "이력서",
                "media": [
                    {
                        "type": "image",
                        "src": "assets/study-room/body_image_1.png",
                        "alt": "이력서 예시 이미지",
                    }
                ],
            }
        )

        self.run_validator_with(data)

    def test_missing_required_seed_section_fails(self) -> None:
        data = copy.deepcopy(self.data)
        data["sections"] = [
            section for section in data["sections"] if section["slug"] != "study-room"
        ]

        with self.assertRaises(SystemExit):
            self.run_validator_with(data)


if __name__ == "__main__":
    unittest.main()

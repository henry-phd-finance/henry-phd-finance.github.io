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
        data["sections"].insert(
            6,
            {
                "slug": "extra",
                "label": "Extra",
                "blocks": [{"type": "paragraph", "text": "Optional extra page."}],
            }
        )
        self.validator.EXPECTED_ORDER.insert(6, "extra")
        try:
            self.run_validator_with(data)
        finally:
            self.validator.EXPECTED_ORDER.remove("extra")

    def test_missing_required_seed_section_fails(self) -> None:
        data = copy.deepcopy(self.data)
        data["sections"] = [
            section for section in data["sections"] if section["slug"] != "recognition"
        ]

        with self.assertRaises(SystemExit):
            self.run_validator_with(data)


if __name__ == "__main__":
    unittest.main()

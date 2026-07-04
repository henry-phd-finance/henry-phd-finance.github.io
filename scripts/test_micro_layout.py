#!/usr/bin/env python3
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MicroLayoutTest(unittest.TestCase):
    def test_renderer_supports_aligned_label_value_rows(self) -> None:
        app_js = (ROOT / "app.js").read_text(encoding="utf-8")
        styles_css = (ROOT / "styles.css").read_text(encoding="utf-8")

        self.assertIn("info-list", app_js)
        self.assertIn("info-row", app_js)
        self.assertIn(".info-list", styles_css)
        self.assertIn(".info-row", styles_css)

    def test_resume_and_cv_headings_do_not_use_pipe_separators(self) -> None:
        for document in ["resume_kr.md", "resume_en.md", "cv_kr.md"]:
            with self.subTest(document=document):
                markdown = (ROOT / "assets" / "documents" / document).read_text(
                    encoding="utf-8"
                )
                pipe_headings = [
                    line
                    for line in markdown.splitlines()
                    if re.match(r"^#{2,4}\s+", line) and " | " in line
                ]
                self.assertEqual(pipe_headings, [])

    def test_cv_uses_record_sections_instead_of_markdown_tables(self) -> None:
        markdown = (ROOT / "assets" / "documents" / "cv_kr.md").read_text(
            encoding="utf-8"
        )
        table_lines = [
            line
            for line in markdown.splitlines()
            if line.strip().startswith("|") and line.strip().endswith("|")
        ]

        self.assertEqual(table_lines, [])
        self.assertIn("### KAIST 경영공학부", markdown)
        self.assertIn(
            "### 광프로파일을 이용한 화면표시장치의 광분포 시뮬레이션 방법 및 화질 최적 광학옵션 탐색 시스템",
            markdown,
        )

    def test_cv_education_uses_transcript_backed_gpa_selectively(self) -> None:
        markdown = (ROOT / "assets" / "documents" / "cv_kr.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("- GPA: 3.97/4.3 (96.70/100)", markdown)
        self.assertIn("- GPA: 3.79/4.3 (94.90/100)", markdown)
        self.assertNotIn("3.27/4.3", markdown)

    def test_cv_professional_experience_uses_timeline_rows(self) -> None:
        markdown = (ROOT / "assets" / "documents" / "cv_kr.md").read_text(
            encoding="utf-8"
        )
        professional_experience = markdown.split("## Selected Projects", maxsplit=1)[0]

        self.assertIn("#### 조직 이동 및 담당 영역", professional_experience)
        self.assertNotIn("경력 흐름:", professional_experience)
        self.assertNotIn("경력 참고:", professional_experience)
        self.assertNotIn(" | ", professional_experience)
        self.assertIn("- 2018.09 ~ 2020.12:", professional_experience)
        self.assertIn("- 참고: 2024.04 ~ 2024.11 육아휴직", professional_experience)


if __name__ == "__main__":
    unittest.main()

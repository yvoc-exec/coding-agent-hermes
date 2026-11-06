"""Offline structural tests for the bundled popular-web-designs skill."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "coding" / "popular-web-designs"


class PopularWebDesignsTests(unittest.TestCase):
    def test_manifest_includes_skill_path(self):
        manifest = (ROOT / "distribution.yaml").read_text(encoding="utf-8")
        self.assertIn("skills/coding/", manifest)

    def test_skill_metadata_and_navigation(self):
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: popular-web-designs\n"))
        self.assertIn("license: MIT", skill)
        self.assertIn('skill_view(name="popular-web-designs"', skill)

    def test_all_catalog_templates_are_bundled(self):
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        expected = re.findall(r"(?m)^\| `([^`]+\.md)` \|", skill)
        self.assertEqual(len(expected), 54)
        self.assertEqual(len(set(expected)), 54)
        directory = SKILL_DIR / "templates"
        actual = {path.name for path in directory.glob("*.md")}
        self.assertEqual(actual, set(expected))
        for name in expected:
            with self.subTest(template=name):
                path = directory / name
                self.assertTrue(path.is_file())
                self.assertGreater(len(path.read_text(encoding="utf-8")), 1000)


if __name__ == "__main__":
    unittest.main()

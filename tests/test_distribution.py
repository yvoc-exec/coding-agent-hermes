"""Dependency-free static contracts for the NOVA CODE Hermes distribution."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def test_files_and_skill_frontmatter(self):
        must_exist = [
            "SOUL.md", "config.yaml", "distribution.yaml", "README.md",
            "skins/forge.yaml", "skills/coding/coding-agent/SKILL.md",
            "knowledge/methodology/operating-loop.md",
            "knowledge/methodology/deep-analysis.md",
            "knowledge/rules/execution.md",
            "knowledge/rules/workspace.md",
            "knowledge/rules/delegation.md",
            "knowledge/rules/derived-skills.md",
            "tests/ACCEPTANCE.md",
        ]
        for item in must_exist:
            with self.subTest(file=item):
                self.assertTrue((ROOT / item).is_file(), item)
        skill_paths = sorted((ROOT / "skills/coding").rglob("SKILL.md"))
        self.assertGreaterEqual(len(skill_paths), 19)
        names = set()
        for p in skill_paths:
            content = p.read_text(encoding="utf-8")
            with self.subTest(skill=str(p.relative_to(ROOT))):
                self.assertTrue(content.startswith("---\n"))
                header = content.split("---", 2)[1]
                match = re.search(r"(?m)^name: ([a-z0-9-]+)$", header)
                self.assertIsNotNone(match)
                self.assertIn("description:", header)
                if match:
                    self.assertNotIn(match.group(1), names)
                    names.add(match.group(1))
                self.assertGreater(len(content), 250)

    def test_manifest_and_model_independence(self):
        manifest = (ROOT / "distribution.yaml").read_text(encoding="utf-8")
        config = (ROOT / "config.yaml").read_text(encoding="utf-8")
        soul = (ROOT / "SOUL.md").read_text(encoding="utf-8")
        self.assertRegex(manifest, r"(?m)^name: coding-agent$")
        self.assertIn("skills/coding/", manifest)
        self.assertIn("knowledge/", manifest)
        self.assertIn("skin: forge", config)
        self.assertRegex(config, r"(?m)^  max_concurrent_children: 4$")
        self.assertRegex(config, r"(?m)^  max_spawn_depth: 1$")
        self.assertIn("orchestrator_enabled: false", config)
        self.assertIn("fallback_providers: []", config)
        self.assertNotRegex(config, r"(?m)^model:\s*$")
        self.assertIn("curator:\n  enabled: false", config)
        self.assertIn("background_review:\n    enabled: false", config)
        self.assertIn("no mandatory delegation", soul.lower())
        self.assertIn("no Senior Advisor", soul)
        self.assertIn("`.coding-agent/WORKSPACE.md`", soul)

    def test_reference_security_and_scope(self):
        soul = (ROOT / "SOUL.md").read_text(encoding="utf-8")
        self.assertIn("Never by default: `git commit`", soul)
        self.assertIn("Read only the specific domain", soul)
        self.assertIn("a failed child route", soul.lower())
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("hermes profile install .", readme)
        self.assertIn("hermes -p coding-agent chat", readme)
        self.assertNotIn("pentest-advisor-agent", soul + readme)
        self.assertNotIn("kanban_create", soul + readme)
        self.assertFalse(any((ROOT / p).exists() for p in ("auth.json", ".env", "mcp.json")))


if __name__ == "__main__":
    unittest.main()

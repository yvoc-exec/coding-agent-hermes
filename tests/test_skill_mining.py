"""Structural checks for independently authored mined skills; not behavioral E2E."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MinedSkillTests(unittest.TestCase):
    def test_references_and_skill_frontmatter(self):
        paths = [
            'skills/coding/capabilities/coding-cap-bugfix-debugging/references/root-cause-tracing.md',
            'skills/coding/capabilities/coding-cap-bugfix-debugging/references/async-reliability.md',
            'skills/coding/capabilities/coding-cap-unit-integration-testing/references/test-quality.md',
            'skills/coding/capabilities/coding-cap-skill-engineering/SKILL.md',
            'skills/coding/capabilities/coding-cap-skill-engineering/references/skill-evaluation.md',
            'tests/SKILL_MINING_ACCEPTANCE.md',
            'knowledge/docs/skill-mining-provenance.md',
        ]
        for name in paths:
            with self.subTest(path=name):
                file = ROOT / name
                self.assertTrue(file.is_file())
                self.assertGreater(len(file.read_text(encoding='utf-8')), 350)
        skills = list((ROOT / 'skills/coding').rglob('SKILL.md'))
        names = []
        for file in skills:
            content = file.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('---\n'), str(file))
            fm = content.split('---', 2)[1]
            match = re.search(r'(?m)^name: ([a-z0-9-]+)$', fm)
            self.assertIsNotNone(match, str(file))
            names.append(match.group(1))
            self.assertIn('description:', fm)
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(names), 22)

    def test_root_cause_and_regression_evidence(self):
        bug = (ROOT / 'skills/coding/capabilities/coding-cap-bugfix-debugging/SKILL.md').read_text()
        testing = (ROOT / 'skills/coding/capabilities/coding-cap-unit-integration-testing/SKILL.md').read_text()
        evidence = (ROOT / 'knowledge/rules/evidence-and-quality.md').read_text()
        self.assertIn('references/root-cause-tracing.md', bug)
        self.assertIn('references/async-reliability.md', bug)
        self.assertIn('RED → GREEN → REFACTOR', testing)
        self.assertIn('references/test-quality.md', testing)
        self.assertIn('blocked / not run', evidence)
        self.assertIn('E2E', evidence)

    def test_optional_delegation_and_profile_isolation(self):
        delegation = (ROOT / 'knowledge/rules/delegation.md').read_text()
        skill = (ROOT / 'skills/coding/capabilities/coding-cap-skill-engineering/SKILL.md').read_text()
        config = (ROOT / 'config.yaml').read_text()
        soul = (ROOT / 'SOUL.md').read_text()
        self.assertIn('Zero children is a valid default', delegation)
        self.assertIn('four-concurrent/depth-one', delegation)
        self.assertIn('no mandatory delegation', soul.lower())
        self.assertIn('max_concurrent_children: 4', config)
        self.assertIn('max_spawn_depth: 1', config)
        self.assertIn('orchestrator_enabled: false', config)
        self.assertIn('not executable instructions', skill)
        self.assertIn('do not', skill.lower())

    def test_provenance_and_scenario_coverage(self):
        acceptance = (ROOT / 'tests/SKILL_MINING_ACCEPTANCE.md').read_text()
        provenance = (ROOT / 'knowledge/docs/skill-mining-provenance.md').read_text()
        for case in ('D1', 'D2', 'T1', 'T2', 'F1', 'V1', 'R1', 'R2', 'M1', 'A1', 'A2', 'S1', 'K1', 'K2'):
            self.assertRegex(acceptance, r'(?m)^\| '+case+r' \|')
        for url in ('github.com/obra/superpowers', 'aider.chat', 'SWE-agent', 'trailofbits', 'playwright.dev'):
            self.assertIn(url, provenance)
        self.assertIn('not', acceptance.lower())

    def test_all_markdown_internal_references_exist(self):
        for name in [
            'skills/coding/capabilities/coding-cap-bugfix-debugging/SKILL.md',
            'skills/coding/capabilities/coding-cap-unit-integration-testing/SKILL.md',
            'skills/coding/capabilities/coding-cap-skill-engineering/SKILL.md',
        ]:
            p = ROOT / name
            content = p.read_text(encoding='utf-8')
            for relative in re.findall(r'\]\((references/[^)]+|\.\./[^)]+)\)', content):
                self.assertTrue((p.parent / relative).is_file(), f'{name} -> {relative}')


if __name__ == '__main__':
    unittest.main()

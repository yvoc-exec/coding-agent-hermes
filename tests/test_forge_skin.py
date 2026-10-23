"""Static regression tests for the dedicated NOVA CODE Hermes skin."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKIN = ROOT / "skins" / "forge.yaml"
CONFIG = ROOT / "config.yaml"
MANIFEST = ROOT / "distribution.yaml"


def luminance(color):
    channels = [
        int(color[index:index + 2], 16) / 255
        for index in (1, 3, 5)
    ]
    linear = [
        value / 12.92 if value <= 0.04045
        else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return sum(
        channel * weight
        for channel, weight in zip(
            linear,
            (0.2126, 0.7152, 0.0722),
        )
    )


def contrast_ratio(first, second):
    a, b = luminance(first), luminance(second)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


class ForgeSkinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skin = SKIN.read_text(encoding="utf-8")
        cls.config = CONFIG.read_text(encoding="utf-8")
        cls.manifest = MANIFEST.read_text(encoding="utf-8")

    def test_skin_identity(self):
        self.assertRegex(self.skin, r"(?m)^name: forge$")
        self.assertIn('agent_name: "NOVA CODE"', self.skin)
        self.assertIn('response_label: " NOVA CODE "', self.skin)
        self.assertNotIn("PENTEST AGENT", self.skin)

    def test_expected_skin_sections(self):
        for section in (
            "colors:",
            "spinner:",
            "branding:",
            "tool_prefix:",
            "tool_emojis:",
            "banner_logo: |",
            "banner_hero: |",
        ):
            with self.subTest(section=section):
                self.assertIn(section, self.skin)

    def test_color_schema_and_hex_values(self):
        match = re.search(
            r"(?ms)^colors:\n(.*?)(?=^[^\s#]|\Z)",
            self.skin,
        )
        self.assertIsNotNone(match)
        body = match.group(1)

        rows = re.findall(
            r'^  ([a-z_]+): "(#[0-9A-Fa-f]{6})"$',
            body,
            re.MULTILINE,
        )
        keys = [key for key, _ in rows]

        self.assertEqual(len(rows), 44)
        self.assertEqual(len(keys), len(set(keys)))

        declared = re.findall(
            r"(?m)^  [a-z_]+:",
            body,
        )
        self.assertEqual(len(declared), len(rows))

    def test_distinct_coding_palette(self):
        self.assertIn(
            'background: "#101719"',
            self.skin,
        )
        self.assertIn(
            'ui_accent: "#87BAA7"',
            self.skin,
        )
        self.assertNotIn(
            'ui_accent: "#7B95AF"',
            self.skin,
        )
        self.assertIn(
            "ENGINEERING",
            self.skin,
        )

    def test_diff_contrast(self):
        colors = dict(re.findall(
            r'^  (diff_(?:added|removed)(?:_word)?): '
            r'"(#[0-9A-Fa-f]{6})"$',
            self.skin,
            re.MULTILINE,
        ))

        self.assertEqual(len(colors), 4)

        for name in ("added", "removed"):
            with self.subTest(highlight=name):
                ratio = contrast_ratio(
                    colors[f"diff_{name}"],
                    colors[f"diff_{name}_word"],
                )
                self.assertGreaterEqual(ratio, 7.0)

    def test_tui_display_contract(self):
        expected = (
            "display:\n"
            "  show_reasoning: false\n"
            "  interface: tui\n"
            "  skin: forge\n"
            "  details_mode: collapsed\n"
            "  sections:\n"
            "    thinking: hidden\n"
            "    tools: expanded\n"
            "    subagents: collapsed\n"
            "    activity: hidden\n"
            "  mouse_tracking: buttons\n"
            "  tui_status_indicator: unicode\n"
        )
        self.assertIn(expected, self.config)

    def test_distribution_ownership(self):
        self.assertIn(
            "  - skins/forge.yaml",
            self.manifest,
        )
        self.assertNotIn(
            "  - skins/nova.yaml",
            self.manifest,
        )

    def test_no_custom_css(self):
        self.assertNotIn("customCSS:", self.skin)


if __name__ == "__main__":
    unittest.main()

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.tension import tension_keywords, tension_stage


class TestTensionAnalysis(unittest.TestCase):
    def test_keywords_contains_basic_terms(self):
        words = tension_keywords()
        self.assertIn("Zagon", words)
        self.assertIn("Razpad", words)

    def test_tension_stage(self):
        self.assertEqual(tension_stage(0.05), "Zagon")
        self.assertEqual(tension_stage(0.5), "Omejitev")
        self.assertEqual(tension_stage(0.9), "Reakcija")


if __name__ == "__main__":
    unittest.main()

import os
import sys
import unittest

# Ensure package root is on path when tests are executed directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.translator import Translator, EternalAnalysis


class TestTranslator(unittest.TestCase):
    def test_basic_translation(self):
        t = Translator("T")
        res = t.translate("Pozdravljeni", "Angle\u0161\u010dina")
        self.assertIn("English", res)
        self.assertEqual(t.history[-1][1], "Angle\u0161\u010dina")

    def test_eternal_analysis(self):
        t = Translator("T")
        analyzer = EternalAnalysis()
        t.translate("Resnica", "Angle\u0161\u010dina")
        record = t.history[-1]
        analysis = analyzer.analyze(record)
        self.assertIn("Analiza prevoda", analysis)
        self.assertEqual(len(analyzer.records), 1)


if __name__ == "__main__":
    unittest.main()

import unittest
from divine_agents.language_model import LanguageModel


class TestLanguageModel(unittest.TestCase):
    def test_language_transition(self):
        lm = LanguageModel()
        msg = lm.transition_language("angle\u0161\u010dina")
        self.assertEqual(lm.language, "angle\u0161\u010dina")
        self.assertIn("\u221a", msg)
        self.assertTrue(lm.agent.name.startswith("EJ-angle"))

    def test_synthesis(self):
        lm = LanguageModel("sloven\u0161\u010dina")
        msg = lm.synthesis("angle\u0161\u010dina")
        self.assertEqual(lm.language, "sinteti\u010dni jezik")
        self.assertIn("\u03a9", msg)


if __name__ == "__main__":
    unittest.main()

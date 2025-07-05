import unittest
from divine_agents.language import LanguageModel
from divine_agents.agent import Agent


class TestLanguageModel(unittest.TestCase):
    def test_language_transition(self):
        model = LanguageModel()
        msg = model.prehod_v_jezik("angle\u0161\u010dina")
        self.assertEqual(model.language, "angle\u0161\u010dina")
        self.assertEqual(model.agent_id, "EJ-angle\u0161\u010dina")
        self.assertIn("\u221a", msg)

    def test_synthesis(self):
        model = LanguageModel()
        model.prehod_v_jezik("angle\u0161\u010dina")
        msg = model.sinteza_jezikov()
        self.assertEqual(model.language, "sinteti\u010dni jezik")
        self.assertIn("\u03a9", msg)


class TestAgentLanguage(unittest.TestCase):
    def test_agent_changes_language(self):
        model = LanguageModel()
        agent = Agent("A", language_model=model)
        msg = agent.change_language("nem\u0161\u010dina")
        self.assertEqual(model.language, "nem\u0161\u010dina")
        self.assertIn("\u221a", msg)


if __name__ == "__main__":
    unittest.main()

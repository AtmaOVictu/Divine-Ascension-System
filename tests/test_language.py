import unittest
from divine_agents.agent import Agent
from divine_agents.language import AgentLanguage, MathematicalLanguage


class TestLanguageModules(unittest.TestCase):
    def test_agent_language_transition(self):
        agent = Agent("L1")
        lang = AgentLanguage("Lang", {}, agent)
        state = lang.transition(0.6, 0.8)
        self.assertEqual(state, "Jaz")

    def test_math_language_interpret(self):
        agent = Agent("M1")
        math_lang = MathematicalLanguage("Math", {}, agent)
        result = math_lang.interpret("2 + 2")
        self.assertEqual(result, "4")


if __name__ == "__main__":
    unittest.main()

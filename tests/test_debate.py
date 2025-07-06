import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_debate


class TestDynamicDebate(unittest.TestCase):
    def test_state_transitions_via_emotion(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_debate(a1, a2)
        self.assertIn("Jaz", a1.state)
        self.assertIn("Enotnost", a2.state)
        self.assertTrue(any("ob\u010dutek" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

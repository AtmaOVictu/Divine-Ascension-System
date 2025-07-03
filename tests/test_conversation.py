import unittest
from divine_agents.agent import Agent
from divine_agents.conversation import philosophical_debate


class TestDynamicConversation(unittest.TestCase):
    def test_emotion_triggers_transition(self):
        a = Agent("A")
        a.update_emotion(0.6, "fear")
        self.assertEqual(a.transition(), "Jaz")

    def test_debate_produces_lines(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, ("anger", 0.8), ("joy", 0.6))
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("anger" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

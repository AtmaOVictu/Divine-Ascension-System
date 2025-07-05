import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate


class TestEmotionTransitions(unittest.TestCase):
    def test_emotion_trigger(self):
        agent = Agent("A")
        agent.feel("fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_debate_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, "anger", "joy")
        self.assertTrue(any("ob\u010duti" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

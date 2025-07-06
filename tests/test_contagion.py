import unittest
from divine_agents.agent import AgentWithHistory
from divine_agents.emotional_contagion import EmotionalContagion


class TestEmotionalContagion(unittest.TestCase):
    def test_spread_emotion(self):
        a1 = AgentWithHistory('A1')
        a2 = AgentWithHistory('A2')
        contagion = EmotionalContagion()
        contagion.add_agent(a1)
        contagion.add_agent(a2)
        a1.update_emotion(0.6)
        contagion.spread_emotion(0, 0.2)
        self.assertGreaterEqual(a2.emotion, 0.8)


if __name__ == '__main__':
    unittest.main()

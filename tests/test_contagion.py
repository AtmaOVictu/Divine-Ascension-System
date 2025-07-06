import unittest
from divine_agents.agent import Agent
from divine_agents.contagion import EmotionalContagion


class TestEmotionalContagion(unittest.TestCase):
    def test_emotion_spread(self):
        a1 = Agent("A1", emotion=0.4)
        a2 = Agent("A2")
        ec = EmotionalContagion()
        ec.add_agent(a1)
        ec.add_agent(a2)
        ec.spread_emotion(0, 0.5)
        self.assertGreater(a2.emotion, 0.4)
        self.assertGreater(a2.tension, 0.4)


if __name__ == "__main__":
    unittest.main()

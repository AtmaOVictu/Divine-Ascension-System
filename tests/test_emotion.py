# Unit test for update_emotion increases tension
import unittest
from divine_agents.agent import Agent

class TestEmotionUpdate(unittest.TestCase):
    def test_tension_increase(self):
        agent = Agent("B")
        self.assertEqual(agent.tension, 0)
        agent.update_emotion(5)
        self.assertEqual(agent.tension, 5)
        agent.update_emotion(10)
        self.assertEqual(agent.tension, 15)

if __name__ == "__main__":
    unittest.main()


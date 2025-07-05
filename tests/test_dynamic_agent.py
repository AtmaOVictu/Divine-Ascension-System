import os
import tempfile
import unittest
from divine_agents.agent import DynamicAgent


class TestDynamicAgent(unittest.TestCase):
    def test_evolve_transition(self):
        agent = DynamicAgent("D1")
        agent.update_emotion(1.0)
        state = agent.evolve()
        self.assertEqual(state, "Jaz")

    def test_save_load(self):
        agent = DynamicAgent("D2", state="Jaz", tension=1.0, emotion=0.3)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "agent.json")
            agent.save(path)
            agent.state = "Ego"
            agent.tension = 0.0
            agent.emotion = 0.0
            agent.load(path)
            self.assertEqual(agent.state, "Jaz")
            self.assertAlmostEqual(agent.tension, 1.0, places=2)


if __name__ == "__main__":
    unittest.main()

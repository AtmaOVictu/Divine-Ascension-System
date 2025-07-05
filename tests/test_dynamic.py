import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.dynamic import DynamicAgent, MultiAgentSystem, logistic


class TestDynamicAgent(unittest.TestCase):
    def test_logistic(self):
        self.assertLess(logistic(0.0, 1.0, 0.5), 0.5)
        self.assertGreater(logistic(1.0, 1.0, 0.5), 0.5)

    def test_dynamic_transition(self):
        agent = DynamicAgent("A")
        agent.update_emotion(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_system_dialogue(self):
        system = MultiAgentSystem(num_agents=2)
        lines = system.dialogue()
        self.assertEqual(len(lines), 2)
        for line in lines:
            self.assertIn("Resnica", line)


if __name__ == "__main__":
    unittest.main()

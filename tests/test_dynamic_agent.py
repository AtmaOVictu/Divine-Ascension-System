import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from divine_agents.dynamic_agent import DynamicAgent, biological_transition, social_transition


class TestDynamicAgent(unittest.TestCase):
    def test_state_transition_on_emotion(self):
        agent = DynamicAgent(id=1)
        agent.update_emotion(0.6, 0.0)
        agent.evolve()
        self.assertEqual(agent.state, "Jaz")

    def test_biological_transition_output(self):
        result = biological_transition(1.0, 1.0, 0.5)
        self.assertGreater(result, 0.5)

    def test_social_transition_output(self):
        result = social_transition(1.0, 1.5, 0.6)
        self.assertGreater(result, 0.5)


if __name__ == "__main__":
    unittest.main()

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.environment import run_simulation
from divine_agents.agent import Agent


class TestEnvironment(unittest.TestCase):
    def test_run_simulation(self):
        lines = run_simulation()
        self.assertTrue(any("transitions" in line for line in lines))
        self.assertTrue(any("Elapsed time" in line for line in lines))

    def test_state_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()

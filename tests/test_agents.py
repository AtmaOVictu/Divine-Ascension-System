import os
import sys
import unittest

# Ensure repository root is on the import path when tests are run directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_timestamps(self):
        agent = Agent("Hist")
        agent.update_tension(1.0)
        agent.transition()
        last_state, timestamp = agent.get_history()[-1]
        self.assertEqual(last_state, "Jaz")
        self.assertIsInstance(timestamp, float)


if __name__ == '__main__':
    unittest.main()

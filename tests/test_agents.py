import os
import sys
import unittest

# Ensure project root is on sys.path so imports work when tests are run
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.loading import simulate_loading_screen


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

    def test_loading_screen(self):
        lines = simulate_loading_screen("Agent1", max_cycles=3)
        # Verify that progress is reported for each cycle and final message exists
        self.assertEqual(len(lines), 4)
        self.assertIn("Loading Screen končan", lines[-1])


if __name__ == '__main__':
    unittest.main()

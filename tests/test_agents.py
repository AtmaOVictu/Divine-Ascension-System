import os
import sys
import unittest

# Ensure the package can be imported when tests are run directly
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
        agent.set_emotion("joy", 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("(joy)"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

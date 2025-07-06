import os
import sys
import unittest

# Ensure the package can be imported when running tests directly
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

    def test_feedback_tension(self):
        agent = Agent("B")
        agent.feel(0.2)
        self.assertGreater(agent.tension, 0)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(a1.state == "Enotnost" or a2.state == "Enotnost")
        self.assertTrue(lines[-1].startswith("Eden") or lines[-1].startswith("Dialog"))


if __name__ == '__main__':
    unittest.main()

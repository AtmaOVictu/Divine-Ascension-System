import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A", state="Jaz")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "strah")
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
        # Expect at least one transition to appear in the dialogue
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        # The second agent should reach Enotnost
        self.assertIn("Enotnost", lines[-1])


if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys

# Ensure the package can be imported when tests are executed from this folder.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_tension_independent_transition(self):
        """Transition triggered purely by tension level."""
        agent = Agent("A")
        agent.update_tension(0.8)  # above tension threshold only
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_independent_transition(self):
        """Transition triggered purely by emotion level."""
        agent = Agent("B")
        agent.update_emotion(0.6)  # emotion threshold exceeded, tension below 0.7
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
        # Check that transitions are announced correctly
        self.assertIn("A1 prehaja v stanje: Jaz", lines[2])
        self.assertIn("A2 prehaja v stanje: Enotnost", lines[3])
        # Ensure responses reflect the new states
        self.assertIn("relativna", lines[4])
        self.assertIn("eno", lines[5])


if __name__ == '__main__':
    unittest.main()

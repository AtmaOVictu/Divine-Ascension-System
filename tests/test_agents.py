import os
import sys
import unittest

# Ensure the package can be imported when tests run standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(80)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion("joy", 60)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_emotional_response(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion("fear", 10)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure a transition to Enotnost occurs in the conversation
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(lines[0].startswith("A1"), True)


if __name__ == "__main__":
    unittest.main()

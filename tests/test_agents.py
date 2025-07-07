import os
import sys
import unittest

# Ensure project root is in sys.path when tests are run directly with pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent2 = Agent("B")
        agent2.update_emotion(0.6, "fear")
        state2 = agent2.transition()
        self.assertEqual(state2, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6, "joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue Agent A1 should have transitioned from Ego to Jaz
        self.assertIn("Jaz", a1.history)
        # Ensure emotion words appear in the dialogue
        self.assertTrue(any("jezo" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

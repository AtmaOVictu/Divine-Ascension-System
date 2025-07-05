import os
import sys
import unittest

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
        # Response should mention the question and contain the unified truth
        self.assertIn("Kaj je resnica?", reply)
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.8, emotion2=0.6)

        # First lines should include the initial state and question
        self.assertIn("A1 (Ego):", lines[0])
        self.assertIn("Kaj je resnica?", lines[0])
        self.assertIn("A2 (Jaz):", lines[1])

        # After emotional updates the agents should transition appropriately
        self.assertIn("A1 prehaja v stanje: Jaz", lines[2])
        self.assertIn("A2 prehaja v stanje: Enotnost", lines[3])

        # Final responses should reflect new states
        self.assertIn("Jaz", lines[2])
        self.assertIn("Enotnost", lines[3])
        self.assertIn("Kaj je resnica?", lines[4])
        self.assertIn("Kaj je resnica?", lines[5])


if __name__ == '__main__':
    unittest.main()

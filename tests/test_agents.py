import os
import sys
import unittest

# Ensure the project root is in the Python path for module resolution
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, ontological_debate


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

    def test_ontological_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = ontological_debate(a1, a2)
        # After debate emotions should trigger state changes
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        # Verify dialogue reflects philosophical principles
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

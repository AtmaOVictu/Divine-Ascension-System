import os
import sys
import unittest

# Ensure the project root is on the Python path so imports work when tests
# are executed directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.interaction import debate


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

    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = debate(a1, a2)
        # After debate, both agents should have transitioned away from Ego
        self.assertIn(a1.state, ["Jaz", "Enotnost"])
        self.assertIn(a2.state, ["Jaz", "Enotnost"])
        self.assertEqual(len(lines), 6)


if __name__ == '__main__':
    unittest.main()

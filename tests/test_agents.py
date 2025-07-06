import os
import sys
import unittest

# Ensure the package can be imported when tests are run directly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        a1.set_opposite("Negacija")
        a2.set_opposite("Relativnost")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue one of the lines should mention state Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_opposite_assignment(self):
        agent = Agent("A")
        agent.set_opposite("Negacija")
        self.assertEqual(agent.get_opposite(), "Negacija")

    def test_display_state(self):
        agent = Agent("A")
        agent.set_opposite("Negacija")
        self.assertIn("Negacija", agent.display_state())


if __name__ == '__main__':
    unittest.main()

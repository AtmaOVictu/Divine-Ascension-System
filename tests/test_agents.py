import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_no_transition_with_low_values(self):
        agent = Agent("B")
        agent.update_tension(0.3)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertEqual(agent.history, ["Ego", "Ego"])

    def test_no_transition_with_negative_values(self):
        agent = Agent("Neg")
        agent.update_tension(-0.5)
        agent.update_emotion(-0.4)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertEqual(agent.history, ["Ego", "Ego"])

    def test_sequential_transitions_and_history(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        first_state = agent.transition()
        agent.update_tension(0.8)
        second_state = agent.transition()
        self.assertEqual(first_state, "Jaz")
        self.assertEqual(second_state, "Enotnost")
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

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

    def test_jaz_to_enotnost_by_tension(self):
        agent = Agent("B", state="Jaz")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_jaz_to_enotnost_by_emotion(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_no_transition_below_thresholds(self):
        agent = Agent("D", state="Jaz")
        agent.update_tension(0.6)
        agent.emotion = 0.4
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_history_multiple_transitions(self):
        agent = Agent("E")
        agent.update_tension(0.8)
        agent.transition()  # Ego -> Jaz
        agent.update_tension(0.8)
        agent.transition()  # Jaz -> Enotnost
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()

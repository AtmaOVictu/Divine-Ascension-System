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
        self.assertIn("eno", reply)

    def test_resolve_moral_dilemma(self):
        agent = Agent("A", morality="Altruizem")
        answer = agent.resolve_moral_dilemma()
        self.assertIn("dobro drugih", answer)

    def test_display_history(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        history = agent.display_history()
        self.assertIn("Jaz", history)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=1)
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

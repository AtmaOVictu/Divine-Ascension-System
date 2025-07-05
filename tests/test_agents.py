import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.surreal import surreal_transition


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

    def test_surreal_transition(self):
        k_values = [0.5, 0.6, 0.7, 0.8, 1.0, 1.1, 1.2, 1.3, 1.5]
        c_values = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
        states = surreal_transition(0.0, k_values, c_values)
        self.assertEqual(len(states), 9)
        self.assertTrue(all(0 <= s <= 1 for s in states))


if __name__ == '__main__':
    unittest.main()

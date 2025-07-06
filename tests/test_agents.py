import sys
from pathlib import Path
import unittest

# Ensure package root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents import (
    Agent,
    philosophical_dialogue,
    AutomatskiPrehodi,
    QLearningAgent,
)


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


class TestAutomation(unittest.TestCase):
    def test_automatic_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        auto = AutomatskiPrehodi(agent)
        state = auto.preveri_pogoje_za_prehod()
        self.assertEqual(state, "Jaz")

    def test_q_learning_update(self):
        qa = QLearningAgent("Q", actions=["a", "b"])
        qa.update_q_value("s", "a", reward=1.0, next_state="s2")
        self.assertIn("a", qa.q_table["s"])


if __name__ == "__main__":
    unittest.main()

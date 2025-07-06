import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue


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
        self.assertIn("odziv", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotional_dialogue_transition(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = emotional_dialogue(a1, a2, 0.9, 0.6)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertEqual(lines[0].split(":")[0], "B1 (Ego)")


if __name__ == '__main__':
    unittest.main()

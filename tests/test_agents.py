import sys
import os
import unittest

# Ensure package is importable when running tests directly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self) -> None:
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self) -> None:
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.9, "strah")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self) -> None:
        agent = Agent("C", state="Enotnost", emotion_name="mir")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self) -> None:
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

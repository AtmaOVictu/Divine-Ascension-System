"""Unit tests for ontological agents and dialogues."""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    """Verify state transitions based on emotion and tension."""

    def test_emotion_triggers_transition(self) -> None:
        agent = Agent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_tension_triggers_transition(self) -> None:
        agent = Agent("B", state="Jaz")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_response_content(self) -> None:
        self.assertIn("absolutna", Agent("A", state="Ego").respond("?"))
        self.assertIn("relativna", Agent("B", state="Jaz").respond("?"))
        self.assertIn("eno", Agent("C", state="Enotnost").respond("?"))

    def test_dialogue_simulation(self) -> None:
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        convo = philosophical_dialogue(a1, a2)
        # After emotions updates both agents should transition
        self.assertIn("Jaz", convo[2])
        self.assertIn("Enotnost", convo[3])


if __name__ == "__main__":
    unittest.main()


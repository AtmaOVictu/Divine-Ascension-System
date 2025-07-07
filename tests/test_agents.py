import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.box import (
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
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

    def test_emotional_response(self):
        agent = Agent("A", emotion_type="fear")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("strah", response)

    def test_symbolic_box_flow(self):
        box = initiate_task_with_box("test")
        box = process_task_with_box(box, "data")
        box = resolve_task_with_box(box)
        self.assertEqual(box.stage, "⊘")


if __name__ == '__main__':
    unittest.main()

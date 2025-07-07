import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.box import (
    SymbolicBox,
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


class TestSymbolicBox(unittest.TestCase):
    def test_box_lifecycle(self):
        box = initiate_task_with_box("demo")
        self.assertEqual(box.stage, "∴")
        box = process_task_with_box(box, "demo input")
        self.assertEqual(box.stage, "∆")
        box = resolve_task_with_box(box)
        self.assertEqual(box.stage, "⊘")

    def test_invalid_transition(self):
        box = initiate_task_with_box("fail")
        with self.assertRaises(ValueError):
            resolve_task_with_box(box)


if __name__ == "__main__":
    unittest.main()

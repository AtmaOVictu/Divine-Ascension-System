import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.boxes import SymbolicBox, RecursiveSymbolicBox


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


class TestBoxes(unittest.TestCase):
    def test_symbolic_box_zero(self):
        box = SymbolicBox(stage="∴")
        self.assertEqual(box.get_data()["initial_state"], 0)

    def test_recursive_box_zero(self):
        inner = RecursiveSymbolicBox(stage="∴")
        outer = RecursiveSymbolicBox(stage="∴", nested_boxes=[inner])
        data = outer.unpack_knowledge()
        self.assertEqual(data["data"]["initial_state"], 0)
        self.assertEqual(data["nested_boxes"][0]["data"]["initial_state"], 0)


if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.symbolic_box import SymbolicBox


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

    def test_agent_box_updates(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.box.stage, "Jaz")


class TestSymbolicBox(unittest.TestCase):
    def test_empty_data_error(self):
        with self.assertRaises(ValueError):
            SymbolicBox(stage="∴", data={})

    def test_box_transition(self):
        box = SymbolicBox(stage="Ego", data={"task": "x"})
        box.transition("Jaz", {"extra": 1})
        self.assertEqual(box.stage, "Jaz")
        self.assertIn("extra", box.data)


if __name__ == '__main__':
    unittest.main()

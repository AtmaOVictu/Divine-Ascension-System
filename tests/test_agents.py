import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, boxed_philosophical_dialogue
from divine_agents.box import AgentBox


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

    def test_agent_box_transition(self):
        agent = Agent("B")
        box = AgentBox(agent)
        box.update_agent(emotion=0.9)
        new_state = box.transition_agent()
        self.assertEqual(new_state, "Jaz")
        self.assertTrue(box.check_integrity() == "valid")

    def test_boxed_dialogue(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = boxed_philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

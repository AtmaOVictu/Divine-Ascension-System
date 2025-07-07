import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.advanced_agents import (
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)
from divine_agents.dialogue import philosophical_dialogue, extended_dialogue


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


class TestAdvancedAgents(unittest.TestCase):
    def test_reason_agent(self):
        r = ReasonAgent("R")
        r.update_logic(0.8)
        self.assertIn("valid", r.reason("context"))

    def test_interpolation_agent(self):
        i = InterpolationAgent("I", interpolation_level=0.9)
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        self.assertIn("connection", i.interpolate(a1, a2))

    def test_intercontinental_agent(self):
        ic = IntercontinentalizationAgent("IC", reach=0.9)
        a1 = Agent("A1")
        a2 = Agent("A2")
        self.assertIn("Connecting", ic.connect_worlds(a1, a2))

    def test_extended_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = extended_dialogue(a1, a2)
        self.assertTrue(any("Connecting" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

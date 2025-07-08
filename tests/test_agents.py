import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.boxing import BoxingStation, Bit


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

    def test_boxing_station_agent_interaction(self):
        station = BoxingStation()
        a1 = Agent("A1", state="Ego")
        a2 = Agent("A2", state="Jaz")
        station.interaction(a1, a2)
        self.assertIn("Self-Other Reflection Box", station.boxes)

    def test_boxing_station_bit_interaction(self):
        station = BoxingStation()
        b1 = Bit(0)
        b2 = Bit(1)
        station.interaction(b1, b2)
        self.assertIn("Bit Interaction Box", station.boxes)


if __name__ == '__main__':
    unittest.main()

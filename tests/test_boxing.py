import unittest

from divine_agents.agent import Agent
from divine_agents.boxing import BoxingStation, Bit


class TestBoxingStation(unittest.TestCase):
    def test_agent_interaction_box(self):
        station = BoxingStation()
        a1 = Agent("A1", state="Ego")
        a2 = Agent("A2", state="Jaz")
        station.interaction(a1, a2)
        self.assertIn("Self-Other Reflection Box", station.boxes)

    def test_bit_interaction_box(self):
        station = BoxingStation()
        b1 = Bit(0)
        b2 = Bit(1)
        station.interaction(b1, b2)
        self.assertIn("Bit Interaction Box", station.boxes)


if __name__ == "__main__":
    unittest.main()

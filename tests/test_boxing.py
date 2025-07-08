import unittest
from divine_agents.agent import Agent
from divine_agents.boxing import BoxingStation, Bit


class TestBoxingStation(unittest.TestCase):
    def test_agent_interaction(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        station = BoxingStation()
        box = station.interaction(a1, a2)
        self.assertEqual(box, "Self-Other Reflection Box")
        self.assertIn(box, station.boxes)

    def test_bit_interaction(self):
        b0 = Bit(0)
        b1 = Bit(1)
        station = BoxingStation()
        box = station.interaction(b0, b1)
        self.assertEqual(box, "Bit Interaction Box")
        self.assertIn(box, station.boxes)


if __name__ == "__main__":
    unittest.main()

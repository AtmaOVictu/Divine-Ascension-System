import unittest
from divine_agents.simple_agents import BitAgent, AlphabetAgent


class TestBitAgent(unittest.TestCase):
    def test_toggle(self):
        bit = BitAgent("B", 0)
        self.assertEqual(bit.transition(), 1)
        self.assertEqual(bit.transition(), 0)


class TestAlphabetAgent(unittest.TestCase):
    def test_cycle(self):
        alpha = AlphabetAgent("A", "A")
        self.assertEqual(alpha.transition(), "B")
        for _ in range(25):
            last = alpha.transition()
        self.assertEqual(last, "A")


if __name__ == "__main__":
    unittest.main()

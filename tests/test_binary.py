import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.binary import BinaryAgent


class TestBinaryAgent(unittest.TestCase):
    def test_interaction_activates_agents(self):
        a1 = BinaryAgent("A1")
        a2 = BinaryAgent("A2")
        state1, state2 = a1.interact(a2)
        self.assertEqual((state1, state2), (1, 1))


if __name__ == "__main__":
    unittest.main()

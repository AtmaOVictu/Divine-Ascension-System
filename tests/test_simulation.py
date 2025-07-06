import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.simulation import interactive_interplay


class TestInteractiveInterplay(unittest.TestCase):
    def test_interplay_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = interactive_interplay(a1, a2, iterations=2)
        # Ensure transitions occur due to tension increase
        self.assertIn("Jaz", " ".join(lines))
        self.assertTrue(any("preha" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

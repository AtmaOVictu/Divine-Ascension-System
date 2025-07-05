import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.discourses import (
    truth_discourse,
    morality_discourse,
    science_discourse,
    liberation_discourse,
)


class TestDiscourses(unittest.TestCase):
    def test_truth_discourse_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = truth_discourse(a1, a2)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))

    def test_liberation_discourse_enotnost(self):
        a1 = Agent("A1", state="Jaz", emotion=0.6, tension=0.6)
        a2 = Agent("A2", state="Jaz")
        lines = liberation_discourse(a1, a2)
        self.assertIn("Enotnost", a1.state)
        self.assertTrue(any("Enotnost" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

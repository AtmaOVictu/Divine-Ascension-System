import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from divine_agents.agent import Agent
from divine_agents.coincidence import happy_coincidence


class TestHappyCoincidence(unittest.TestCase):
    def test_coincidence_triggers_transition(self):
        random.seed(2)
        a1 = Agent("A1")
        a2 = Agent("A2")
        event, s1, s2 = happy_coincidence(a1, a2)
        self.assertEqual(event, "positive")
        self.assertEqual(s1, "Jaz")
        self.assertEqual(s2, "Jaz")


if __name__ == "__main__":
    unittest.main()

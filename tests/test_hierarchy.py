import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.hierarchy import MainAgent


class TestHierarchy(unittest.TestCase):
    def test_create_and_transition_sub_agent(self):
        main = MainAgent("main")
        sub = main.create_sub_agent("sub", tension=0.8)
        main.transition_sub_agents()
        self.assertEqual(sub.state, "Jaz")


if __name__ == "__main__":
    unittest.main()

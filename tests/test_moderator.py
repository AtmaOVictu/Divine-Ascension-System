import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.moderator import HiddenModerator


class TestHiddenModerator(unittest.TestCase):
    def test_activation(self):
        mod = HiddenModerator("M")
        mod.evaluate_state(tension=0.6, emotion=0.2)
        self.assertEqual(mod.state, "active")

    def test_reveal(self):
        mod = HiddenModerator("M")
        mod.evaluate_state(tension=0.8, emotion=0.1)
        mod.reveal_moderator()
        self.assertEqual(mod.state, "revealed")


if __name__ == "__main__":
    unittest.main()

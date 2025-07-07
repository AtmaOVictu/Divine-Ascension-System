import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.krak import Krak
from divine_agents.dialogue import philosophical_dialogue


class TestKrak(unittest.TestCase):
    def test_krak_transition(self):
        krak = Krak("K")
        krak.update_emotion(0.9)
        state = krak.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("dialogue", krak.task)

    def test_krak_history(self):
        krak = Krak("K")
        krak.update_tension(0.8)
        krak.transition()
        self.assertEqual(len(krak.history), 2)

    def test_dialogue_with_krak(self):
        k1 = Krak("K1")
        k2 = Krak("K2", state="Jaz")
        lines = philosophical_dialogue(k1, k2)
        self.assertTrue(any("nalogo" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

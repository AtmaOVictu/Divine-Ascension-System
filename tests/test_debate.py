import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents import Agent, philosophical_debate


class TestDebate(unittest.TestCase):
    def test_emotion_transition(self):
        a1 = Agent("A1")
        a1.set_emotion('fear', 0.8)
        self.assertEqual(a1.transition(), "Jaz")

    def test_debate_lines(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        joined = "\n".join(lines)
        self.assertIn("absolutna", joined)
        self.assertTrue(any(state in joined for state in ["Jaz", "Enotnost"]))


if __name__ == '__main__':
    unittest.main()

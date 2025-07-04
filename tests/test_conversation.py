import unittest
from divine_agents import Agent, interactive_debate


class TestInteractiveDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = interactive_debate(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        # Ensure philosophical views are present
        joined_lines = " ".join(lines)
        self.assertIn("absolutna", joined_lines)
        self.assertIn("relativna", joined_lines)
        self.assertIn("eno", joined_lines)


if __name__ == '__main__':
    unittest.main()

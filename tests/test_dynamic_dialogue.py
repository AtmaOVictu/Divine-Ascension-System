import unittest
from divine_agents import Agent, dynamic_dialogue


class TestDynamicDialogue(unittest.TestCase):
    def test_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        joined = "\n".join(lines)
        self.assertIn("Jaz", joined)
        self.assertIn("Enotnost", joined)

    def test_initial_responses(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2, rounds=1)
        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents import Agent, DialogueManager


class TestDialogueManager(unittest.TestCase):
    def test_run_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        manager = DialogueManager(a1, a2)
        manager.run([0.4, 0.4, 0.4], [0.8, 0.1, 0.1])
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")

    def test_dialogue_lines(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        manager = DialogueManager(a1, a2)
        lines = manager.run([0.4], [0.8])
        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])


if __name__ == "__main__":
    unittest.main()

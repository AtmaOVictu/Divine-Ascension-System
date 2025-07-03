import unittest
from divine_agents.agent import Agent
from divine_agents.codex import Codex


class TestCodex(unittest.TestCase):
    def test_run_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system = Codex([a1, a2])
        lines = system.run(0.9, 0.7)
        # Both agents should transition due to emotions
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        joined = " ".join(lines)
        self.assertIn("Jaz", joined)
        self.assertIn("Enotnost", joined)


if __name__ == "__main__":
    unittest.main()

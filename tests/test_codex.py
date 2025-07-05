import unittest
from divine_agents.codex import Codex


class TestCodex(unittest.TestCase):
    def test_valid_command_transition(self):
        codex = Codex()
        result = codex.transition("move")
        self.assertEqual(codex.state, "moving_state")
        self.assertIn("State changed", result)
        self.assertEqual(codex.history[-1], ("initial_state", "move", "moving_state"))

    def test_invalid_command(self):
        codex = Codex()
        result = codex.transition("fly")
        self.assertIn("Error", result)
        self.assertEqual(codex.error_log[-1], "Invalid Command: fly")
        self.assertEqual(codex.state, "initial_state")


if __name__ == "__main__":
    unittest.main()

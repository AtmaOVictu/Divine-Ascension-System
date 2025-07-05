import unittest
from divine_agents.agent import Agent
from divine_agents.codex import Codex


class TestCodex(unittest.TestCase):
    def test_invalid_command(self):
        agent = Agent("A")
        codex = Codex(agent)
        response = codex.execute("jump")
        self.assertTrue(response.startswith("Error:"))
        self.assertEqual(len(codex.get_error_log()), 1)

    def test_move_transition(self):
        agent = Agent("A", tension=0.8)
        codex = Codex(agent)
        codex.execute("move")
        self.assertEqual(agent.state, "Jaz")
        self.assertEqual(codex.get_history()[-1][2], "Jaz")

    def test_reset_command(self):
        agent = Agent("A", tension=1.0)
        codex = Codex(agent)
        codex.execute("move")
        codex.execute("reset")
        self.assertEqual(agent.state, "Ego")

    def test_update_command(self):
        agent = Agent("A")
        codex = Codex(agent)
        codex.execute("update", emotion=0.6)
        codex.execute("move")
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()

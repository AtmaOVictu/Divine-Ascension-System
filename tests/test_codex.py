import unittest
from divine_agents.codex import Codex
from divine_agents.agent import Agent


class TestCodex(unittest.TestCase):
    def test_cycle_once(self):
        codex = Codex(stevilo_agentov=2)
        state = codex.cycle_once()
        self.assertEqual(len(state), 2)
        for s in state.values():
            self.assertIn(s, Agent.STATES)


if __name__ == "__main__":
    unittest.main()

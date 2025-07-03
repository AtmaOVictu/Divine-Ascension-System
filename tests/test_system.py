import unittest

from divine_agents.codex import Codex


class TestCodexSystem(unittest.TestCase):
    def test_simulate_dialogue(self):
        system = Codex(stevilo_agentov=2)
        lines = system.simulate_dialogue()
        # After simulation at least one agent should have transitioned
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

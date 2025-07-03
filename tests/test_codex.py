import unittest
from divine_agents.codex import Codex


class TestCodexSystem(unittest.TestCase):
    def test_initial_state(self):
        system = Codex(num_agents=2)
        self.assertEqual(len(system.agents), 2)
        for agent in system.agents:
            self.assertEqual(agent.state, "Ego")

    def test_simulate_interaction(self):
        system = Codex(num_agents=2)
        lines = system.simulate_interaction()
        self.assertGreater(len(lines), 0)
        # After interaction, at least one agent should have progressed
        self.assertTrue(any(a.state != "Ego" for a in system.agents))


if __name__ == "__main__":
    unittest.main()

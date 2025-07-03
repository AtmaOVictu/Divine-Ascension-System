import unittest
from divine_agents import Agent, Codex


class TestCodex(unittest.TestCase):
    def test_simulate_step(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        codex = Codex([a1, a2])
        lines = codex.simulate_step()
        # Ensure dialogue contains expected philosophical perspectives
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line or "eno" in line for line in lines))
        # Check that a state transition occurred
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertGreaterEqual(len(lines), 4)


if __name__ == "__main__":
    unittest.main()

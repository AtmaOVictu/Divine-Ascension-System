import unittest
from divine_agents.agent import Agent
from divine_agents.codex import Codex

class TestCodexDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        codex = Codex()
        lines = codex.debate(a1, a2, turns=2)
        self.assertTrue(len(lines) > 0)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue("Enotnost" in a1.state or "Enotnost" in a2.state)

if __name__ == "__main__":
    unittest.main()

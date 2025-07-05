import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate

class TestDebate(unittest.TestCase):
    def test_debate_reaches_enotnost(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=3)
        self.assertIn("Enotnost", a1.history[-1] + a2.history[-1])
        self.assertTrue(any("prehaja v stanje" in l for l in lines))

if __name__ == "__main__":
    unittest.main()

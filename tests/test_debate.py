import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate


class TestPhilosophicalDebate(unittest.TestCase):
    def test_debate_leads_to_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=2)
        self.assertIn("absolutna", lines[0])
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

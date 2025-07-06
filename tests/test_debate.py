import unittest
from divine_agents import Agent, ontological_debate


class TestOntologicalDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2", state="Jaz")
        lines = ontological_debate(a1, a2, rounds=2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertIn(a2.state, ("Jaz", "Enotnost"))


if __name__ == "__main__":
    unittest.main()

import unittest
from divine_agents import Agent, PhilosophicalDebate


class TestDebate(unittest.TestCase):
    def test_debate_round_causes_transition(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2")
        debate = PhilosophicalDebate(a1, a2)
        lines = debate.run_round()
        # after a single round, both agents should have transitioned from Ego to Jaz
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")
        # ensure dialogue lines mention states
        self.assertTrue(any("Jaz" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

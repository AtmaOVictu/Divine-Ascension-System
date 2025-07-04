import unittest

from divine_agents import Agent, debate


class TestDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = debate(a1, a2, rounds=2)
        self.assertIn("Jaz", a1.history)
        self.assertTrue(any("resnica" in line.lower() for line in lines))


if __name__ == "__main__":
    unittest.main()

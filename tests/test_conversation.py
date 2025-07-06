import unittest
from divine_agents import Agent, debate


class TestDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = debate(a1, a2, turns=2)
        # After two turns at least one agent should reach Enotnost
        self.assertTrue(any("Enotnost" in l for l in lines))
        # Ensure conversation produced multiple lines
        self.assertGreater(len(lines), 0)


if __name__ == '__main__':
    unittest.main()

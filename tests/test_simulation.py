import unittest

from divine_agents import Agent, dynamic_philosophical_debate


class TestDynamicDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_philosophical_debate(a1, a2, rounds=2)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("Vse resnice so eno" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

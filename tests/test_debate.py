import unittest
from divine_agents import Agent, philosophical_debate


class TestPhilosophicalDebate(unittest.TestCase):
    def test_state_transitions_in_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")

        lines = philosophical_debate(a1, a2, [0.8], [0.6])

        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

        self.assertTrue(any("absolutna" in l for l in lines))
        self.assertTrue(any("relativna" in l for l in lines))
        self.assertTrue(any("eno" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

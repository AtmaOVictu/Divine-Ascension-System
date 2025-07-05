import unittest
from divine_agents.paradox import ParadoxicalAgent
from divine_agents.dialogue import paradoxical_dialogue


class TestParadoxicalAgent(unittest.TestCase):
    def test_paradox_questions(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("Ali sem jaz", agent.ask_paradox())
        agent.update_tension(0.8)
        agent.transition()
        self.assertIn("Ali sem to", agent.ask_paradox())

    def test_paradox_dialogue(self):
        a1 = ParadoxicalAgent("A1")
        a2 = ParadoxicalAgent("A2")
        lines = paradoxical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

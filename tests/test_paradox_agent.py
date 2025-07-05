import unittest
from divine_agents.paradox_agent import ParadoxicalAgent
from divine_agents.dialogue import paradoxical_dialogue

class TestParadoxicalAgent(unittest.TestCase):
    def test_ask_paradox(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("Ali sem jaz", agent.ask_paradox())
        agent.update_tension(1.0)
        agent.transition()
        self.assertIn("Ali sem to", agent.ask_paradox())

    def test_dialogue_transition(self):
        a1 = ParadoxicalAgent("A1")
        a2 = ParadoxicalAgent("A2", state="Jaz")
        lines = paradoxical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

if __name__ == '__main__':
    unittest.main()

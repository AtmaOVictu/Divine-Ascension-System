import unittest
from divine_agents.recursive_agent import RecursiveAgent
from divine_agents.dialogue import dynamic_dialogue


class TestRecursiveAgent(unittest.TestCase):
    def test_reflect_triggers_transition(self):
        agent = RecursiveAgent("R1")
        agent.update_tension(0.8)
        agent.reflect()
        self.assertEqual(agent.state, "Jaz")

    def test_dynamic_dialogue(self):
        a1 = RecursiveAgent("A1")
        a2 = RecursiveAgent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(len(lines), 6)


if __name__ == '__main__':
    unittest.main()

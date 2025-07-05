import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import ontological_debate

class TestOntologicalDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = ontological_debate(a1, a2, rounds=2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_express_truth_output(self):
        agent = Agent("B")
        agent.update_emotion(0.8)
        line = agent.express_truth()
        self.assertIn("Ego", line)
        self.assertIn("Resnica", line)

if __name__ == '__main__':
    unittest.main()

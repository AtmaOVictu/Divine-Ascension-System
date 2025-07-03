import unittest
from divine_agents.syntax import SyntaxAgent, create_syntax_agents


class TestSyntaxAgent(unittest.TestCase):
    def test_create_agents(self):
        agents = create_syntax_agents(2)
        self.assertEqual(len(agents), 2)
        self.assertTrue(all(isinstance(a, SyntaxAgent) for a in agents))

    def test_syntax_procedure_transition(self):
        agent = SyntaxAgent("S1")
        new_state = agent.syntax_procedure(emotion=0.6, tension=0.8)
        self.assertEqual(new_state, "Jaz")


if __name__ == "__main__":
    unittest.main()

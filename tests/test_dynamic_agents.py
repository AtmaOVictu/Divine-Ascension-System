import unittest
from divine_agents.dynamic_agent import DynamicAgent, dinamicka_inicializacija


class TestDynamicAgent(unittest.TestCase):
    def test_dynamic_transition(self):
        agent = DynamicAgent("A", tension=0.8, active=True)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_antidynamic_no_transition(self):
        agent = DynamicAgent("B", tension=0.9, agent_type="antidinami\u010den", active=True)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_dinamicka_inicializacija(self):
        a1 = DynamicAgent("A1", aktivnosti=6, active=True)
        a2 = DynamicAgent("A2", aktivnosti=6, active=True)
        dinamicka_inicializacija([a1, a2])
        self.assertIn("A2", a1.connections)
        self.assertIn("A1", a2.connections)


if __name__ == "__main__":
    unittest.main()

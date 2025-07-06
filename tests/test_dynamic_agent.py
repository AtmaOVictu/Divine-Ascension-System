import unittest
from divine_agents.dynamic_agent import DynamicAgent, dinamicka_inicializacija

class TestDynamicAgent(unittest.TestCase):
    def test_dynamic_transition(self):
        agent = DynamicAgent("D", tension=0.8)
        state = agent.prehod()
        self.assertEqual(state, "Jaz")

    def test_antidynamic_stays_ego(self):
        agent = DynamicAgent("A", tension=1.0, tip="antidinami\u010den")
        state = agent.prehod()
        self.assertEqual(state, "Ego")

    def test_dinamicka_inicializacija(self):
        a1 = DynamicAgent("A1", aktivnosti=6)
        a2 = DynamicAgent("A2", aktivnosti=6)
        dinamicka_inicializacija([a1, a2])
        self.assertIn(a2, a1.povezave)
        self.assertIn(a1, a2.povezave)

if __name__ == '__main__':
    unittest.main()

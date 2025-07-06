import unittest
from divine_agents.dynamic_agent import (
    DynamicAgent,
    dinamicka_inicializacija,
    reorganizacija_sistema,
)


class TestDynamicAgent(unittest.TestCase):
    def test_state_transition(self):
        agent = DynamicAgent("A", tension=0.8)
        self.assertEqual(agent.prehod(), "Jaz")

    def test_dinamicka_inicializacija(self):
        a1 = DynamicAgent("A1", stanje="Jaz")
        a2 = DynamicAgent("A2", stanje="Jaz")
        dinamicka_inicializacija([a1, a2])
        self.assertIn(a1, a2.povezave)
        self.assertIn(a2, a1.povezave)

    def test_reorganizacija_sistema(self):
        a1 = DynamicAgent("A1", aktivnosti=11)
        reorganizacija_sistema([a1])
        self.assertEqual(a1.stanje, "reorganizirano")


if __name__ == "__main__":
    unittest.main()

import unittest
from divine_agents.dynamic_agent import (
    DynamicAgent,
    dinamicka_inicializacija,
    reorganizacija_sistema,
)


class TestDynamicAgent(unittest.TestCase):
    def test_reorganizacija(self):
        a1 = DynamicAgent("A1", state="aktiviran", aktivnosti=6)
        a2 = DynamicAgent("A2", state="aktiviran", aktivnosti=6)
        dinamicka_inicializacija([a1, a2])
        self.assertEqual(a1.state, "prehod")
        self.assertIn(a1, a2.povezave)

    def test_reorganizacija_sistema(self):
        agent = DynamicAgent("A", aktivnosti=10)
        reorganizacija_sistema([agent])
        self.assertEqual(agent.state, "reorganizirano")


if __name__ == "__main__":
    unittest.main()

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.dynamic_agent import (
    DynamicAgent,
    dinamicka_inicializacija,
    reorganizacija_sistema,
)


class TestDynamicAgent(unittest.TestCase):
    def test_reorganizacija(self):
        a1 = DynamicAgent("A1", state="aktiviran", aktivnosti=6)
        a2 = DynamicAgent("A2", state="aktiviran", aktivnosti=6)
        agents = dinamicka_inicializacija([a1, a2])
        self.assertEqual(agents[0].state, "prehod")
        self.assertEqual(agents[1].state, "prehod")

    def test_medsebojna_reorganizacija(self):
        a1 = DynamicAgent("A1", state="aktiviran", aktivnosti=6)
        a2 = DynamicAgent("A2", state="aktiviran", aktivnosti=6)
        a1.reorganiziraj(a2)
        self.assertIn(a1, a2.povezave)

    def test_reorganizacija_sistema(self):
        a1 = DynamicAgent("A1", aktivnosti=11)
        reorganizacija_sistema([a1])
        self.assertEqual(a1.state, "reorganizirano")


if __name__ == "__main__":
    unittest.main()

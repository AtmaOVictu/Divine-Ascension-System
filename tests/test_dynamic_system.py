import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.dynamic_agent import DynamicAgent
from divine_agents.system import dinamicka_inicializacija


class TestDynamicAgent(unittest.TestCase):

    def test_prehod(self):
        agent = DynamicAgent("A", tension=0.8)
        self.assertEqual(agent.prehod(), "Jaz")
        agent = DynamicAgent("B", emotion=0.6)
        self.assertEqual(agent.prehod(), "Enotnost")

    def test_reorganizacija(self):
        agent1 = DynamicAgent("A1", stanje="aktiviran", aktivnosti=6)
        agent2 = DynamicAgent("A2", stanje="aktiviran", aktivnosti=6)
        agenti = [agent1, agent2]
        dinamicka_inicializacija(agenti)
        self.assertEqual(agent1.stanje, "prehod")
        self.assertEqual(agent2.stanje, "prehod")
        self.assertIn(agent1, agent2.povezave)
        self.assertIn(agent2, agent1.povezave)


if __name__ == "__main__":
    unittest.main()

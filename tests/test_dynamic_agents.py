import unittest
from divine_agents.dynamic_agent import DynamicAgent, dinamicka_inicializacija

class TestDynamicAgent(unittest.TestCase):
    def test_dynamic_transition(self):
        agent = DynamicAgent("A", state="Ego", tip="dinamičen")
        agent.update_tension(0.8)
        state = agent.prehod()
        self.assertEqual(state, "Jaz")

    def test_dinamika_in_antidinamicnost(self):
        agent1 = DynamicAgent("Agent 1", aktivnosti=6)
        agent2 = DynamicAgent("Agent 2", aktivnosti=6)
        agenti = dinamicka_inicializacija([agent1, agent2])
        self.assertEqual(agent1.state, "prehod")
        self.assertEqual(agent2.state, "prehod")

    def test_antidinamicen_agent(self):
        agent1 = DynamicAgent("A1", state="Ego", tip="antidinamičen")
        agent2 = DynamicAgent("A2", state="Ego", tip="antidinamičen")
        agenti = dinamicka_inicializacija([agent1, agent2])
        self.assertEqual(agent1.state, "Ego")
        self.assertEqual(agent2.state, "Ego")

if __name__ == "__main__":
    unittest.main()

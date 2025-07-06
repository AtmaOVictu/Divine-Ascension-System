import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_philosophical_dialogue
from divine_agents.dynamic_agent import DynamicAgent, dinamicka_inicializacija


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestDynamicAgent(unittest.TestCase):
    def test_dynamic_transition(self):
        agent = DynamicAgent("D1", tip="dinamičen")
        agent.update_tension(0.9)
        self.assertEqual(agent.transition(), "Jaz")

    def test_antidynamic_no_transition(self):
        agent = DynamicAgent("D2", tip="antidinamičen")
        agent.update_tension(1.0)
        self.assertEqual(agent.transition(), "Ego")

    def test_dinamicka_inicializacija(self):
        a1 = DynamicAgent("A1", state="Jaz", tip="dinamičen", aktivnosti=6)
        a2 = DynamicAgent("A2", state="Jaz", tip="dinamičen", aktivnosti=6)
        dinamicka_inicializacija([a1, a2])
        self.assertIn(a2, a1.povezave)

    def test_dynamic_dialogue(self):
        a1 = DynamicAgent("AA1", tip="dinamičen")
        a2 = DynamicAgent("AA2", state="Jaz", tip="dinamičen")
        lines = dynamic_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

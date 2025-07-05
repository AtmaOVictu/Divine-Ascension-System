import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.primary_agent import PraviPrimarniAgent, Stance, InstancaAgenta


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


class TestPrimaryAgents(unittest.TestCase):
    def test_instanca_agenta(self):
        agent = InstancaAgenta("Agent 3", "stabilno", 0.5, 0.5, 0.5, 3)
        self.assertEqual(agent.trenutni_tedenski_nivo, 3)
        agent.prehod_v_novo_fazo()
        self.assertEqual(agent.faza, "tedenski nivo 3")

    def test_stance_execution(self):
        agent = PraviPrimarniAgent("Agent 1", "prehod", 0.6, 0.4, 0.4)
        stance = Stance("Moralni princip", "Odgovornost za odločitve")
        result = stance.izvajaj_stance(agent)
        self.assertIn("Odgovornost", result)


if __name__ == '__main__':
    unittest.main()

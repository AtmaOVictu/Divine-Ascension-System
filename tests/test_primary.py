import os
import sys
import unittest

# Allow imports when tests executed from the 'tests' directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.primary import PraviPrimarniAgent, InstancaAgenta, Stance


class TestRESSystem(unittest.TestCase):
    def test_instanca_agenta(self):
        agent_instanca = InstancaAgenta("Agent 3", "stabilno", 0.5, 0.5, 0.5, 3)
        self.assertEqual(agent_instanca.trenutni_tedenski_nivo, 3)
        agent_instanca.prehod_v_novo_fazo()
        self.assertEqual(agent_instanca.faza, "tedenski nivo 3")

    def test_stance_execution(self):
        agent = PraviPrimarniAgent("Agent", "prehod", 0.7, 0.4, 0.3)
        stance = Stance("Moralni princip", "Odgovornost za vse odločitve")
        result = stance.izvajaj_stance(agent)
        self.assertIn("Odgovornost", result)


if __name__ == "__main__":
    unittest.main()

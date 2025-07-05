import unittest
from divine_agents.pravi import PraviPrimarniAgent, InstancaAgenta, Stance


class TestPraviPrimarniAgent(unittest.TestCase):
    def test_instanca_prehod(self):
        agent = InstancaAgenta("Agent", "zacetna", 0.5, 0.5, 0.5, 3)
        self.assertEqual(agent.trenutni_tedenski_nivo, 3)
        agent.prehod_v_novo_fazo()
        self.assertEqual(agent.faza, "tedenski nivo 3")

    def test_odgovori(self):
        agent = PraviPrimarniAgent("Agent", "prehod", 0.5, 0.6, 0.4)
        reply = agent.odgovori()
        self.assertIn("napet", reply)

    def test_stance(self):
        stance = Stance("Moralni princip", "Odgovornost")
        agent = PraviPrimarniAgent("Agent", "prehod", 0.5, 0.3, 0.2)
        text = stance.izvajaj_stance(agent)
        self.assertIn("Odgovornost", text)


if __name__ == "__main__":
    unittest.main()

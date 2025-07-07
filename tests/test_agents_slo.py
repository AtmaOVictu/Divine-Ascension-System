import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentiSlovensko(unittest.TestCase):
    """Preizkusi v slovenskem jeziku."""

    def test_prehod_napetost(self):
        a = Agent("Slavko")
        a.update_tension(0.8)
        stanje = a.transition()
        self.assertEqual(stanje, "Jaz")

    def test_odgovor_custva(self):
        a = Agent("Mira", state="Ego")
        a.update_emotion(0.7)
        a.transition()
        odgovor = a.respond("Kaj je resnica?")
        self.assertIn("čustveno", odgovor)

    def test_dialog_slovenija(self):
        a1 = Agent("Ana")
        a2 = Agent("Boris", state="Jaz")
        vrstice = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja" in line for line in vrstice))

if __name__ == '__main__':
    unittest.main()

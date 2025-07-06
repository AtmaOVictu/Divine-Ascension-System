import unittest
from divine_agents.opposites import OntologicalOppositesGenerator


class TestOppositesGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = OntologicalOppositesGenerator()

    def test_generate_opposites_returns_pair(self):
        pair = self.generator.generate_opposites()
        self.assertIsInstance(pair, tuple)
        self.assertEqual(len(pair), 2)
        self.assertIn(pair[0], self.generator.opposites)
        self.assertEqual(self.generator.opposites[pair[0]], pair[1])

    def test_create_transition_known_state(self):
        result = self.generator.create_transition("tišina")
        self.assertEqual(result, "Prehod iz tišina v zven.")

    def test_create_transition_unknown_state(self):
        result = self.generator.create_transition("neznano")
        self.assertEqual(result, "Nema nasprotja za neznano.")


if __name__ == "__main__":
    unittest.main()

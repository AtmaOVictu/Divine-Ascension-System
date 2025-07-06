import unittest
from divine_agents.opposites import OntologicalOppositesGenerator

class TestOntologicalOppositesGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = OntologicalOppositesGenerator()

    def test_generate_pair(self):
        left, right = self.gen.generate_opposites()
        self.assertIn(left, self.gen.opposites)
        self.assertEqual(self.gen.opposites[left], right)

    def test_get_opposite(self):
        self.assertEqual(self.gen.get_opposite("tišina"), "zven")
        self.assertIsNone(self.gen.get_opposite("unknown"))

if __name__ == "__main__":
    unittest.main()

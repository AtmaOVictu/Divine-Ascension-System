import unittest
from divine_agents.opposites import OntologicalOppositesGenerator

class TestOppositesGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = OntologicalOppositesGenerator()

    def test_generate_pair(self):
        left, right = self.gen.generate_opposites()
        self.assertIn(left, self.gen.opposites)
        self.assertEqual(self.gen.opposites[left], right)

    def test_create_transition(self):
        message = self.gen.create_transition("tišina")
        self.assertIn("zven", message)

if __name__ == '__main__':
    unittest.main()

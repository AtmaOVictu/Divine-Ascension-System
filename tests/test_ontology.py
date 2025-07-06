import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import advanced_dialogue
from divine_agents.ontology import categorize


class TestOntology(unittest.TestCase):
    def test_categorize(self):
        concept = categorize('ljubezen')
        self.assertIsNotNone(concept)
        self.assertEqual(concept.category, 'čustvo')
        self.assertIn('toplina', concept.connotations)

    def test_advanced_dialogue(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = advanced_dialogue(a1, a2, 'svoboda')
        self.assertTrue(lines)
        self.assertEqual(a1.state, 'Jaz')
        self.assertEqual(a2.state, 'Enotnost')
        self.assertIn('kategorijo', lines[0])


if __name__ == '__main__':
    unittest.main()

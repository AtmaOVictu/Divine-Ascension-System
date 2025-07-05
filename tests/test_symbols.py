import unittest
from divine_agents.symbols import OntologicalSymbol, OntologicalSymbolSet


class TestOntologicalSymbolSet(unittest.TestCase):
    def test_add_and_remove(self):
        symbol_set = OntologicalSymbolSet()
        s = OntologicalSymbol('O', 'Potencialnost')
        symbol_set.add_symbol(s)
        self.assertIn('O', symbol_set.symbols)
        symbol_set.remove_symbol('O')
        self.assertNotIn('O', symbol_set.symbols)

    def test_activate_and_transition(self):
        symbol_set = OntologicalSymbolSet()
        s1 = OntologicalSymbol('O', 'Potencialnost')
        s2 = OntologicalSymbol('1', 'Identiteta')
        symbol_set.add_symbol(s1)
        symbol_set.add_symbol(s2)
        activations = symbol_set.activate_all()
        self.assertEqual(len(activations), 2)
        transitions = symbol_set.transition_all({'O': 'Realizacija', '1': 'Enotnost'})
        self.assertEqual(s1.meaning, 'Realizacija')
        self.assertEqual(s2.meaning, 'Enotnost')
        self.assertEqual(len(transitions), 2)


if __name__ == '__main__':
    unittest.main()


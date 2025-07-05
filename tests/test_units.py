import unittest
from divine_agents.units import OntologicalUnit


class TestOntologicalUnit(unittest.TestCase):
    def test_activation(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Mo\u010dan ob\u010dutek naklonjenosti")
        message = unit.activate()
        self.assertIn("aktivirana", message)
        self.assertIn("Mo\u010dan ob\u010dutek naklonjenosti", message)

    def test_transition(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Mo\u010dan ob\u010dutek naklonjenosti")
        msg = unit.transition("Romanti\u010dna ljubezen")
        self.assertIn("Romanti\u010dna ljubezen", unit.meaning)
        self.assertIn("prehaja", msg)


if __name__ == '__main__':
    unittest.main()

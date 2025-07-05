import unittest
from divine_agents.ontological_unit import OntologicalUnit


class TestOntologicalUnit(unittest.TestCase):
    def test_activation_and_transition(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Mo\u010dan ob\u010dutek naklonjenosti")
        unit.activate()
        unit.transition("Romanti\u010dna ljubezen")
        self.assertEqual(unit.meaning, "Romanti\u010dna ljubezen")


if __name__ == "__main__":
    unittest.main()

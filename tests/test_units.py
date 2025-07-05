import unittest
from divine_agents.ontological_unit import OntologicalUnit


class TestOntologicalUnit(unittest.TestCase):
    def test_activation_and_transition(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Mo\u010dan ob\u010dutek naklonjenosti")
        msg = unit.activate()
        self.assertIn("aktivirana", msg)
        transition_msg = unit.transition("Romanti\u010dna ljubezen")
        self.assertIn("Romanti\u010dna ljubezen", transition_msg)
        self.assertEqual(unit.meaning, "Romanti\u010dna ljubezen")

    def test_display(self):
        unit = OntologicalUnit("❤", "ozna\u010dba", "Simbol za ljubezen")
        unit.transition("Simbol za ne\u017enost")
        display = unit.display()
        self.assertIn("Simbol za ne\u017enost", display)


if __name__ == "__main__":
    unittest.main()

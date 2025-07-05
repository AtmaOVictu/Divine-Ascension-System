import unittest
from divine_agents.unit import OntologicalUnit


class TestOntologicalUnit(unittest.TestCase):
    def test_transition_changes_meaning(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Močan občutek")
        unit.transition("Romantična ljubezen")
        self.assertEqual(unit.meaning, "Romantična ljubezen")

    def test_activation_and_display(self):
        unit = OntologicalUnit("❤", "označba", "Simbol")
        # Activation should not change meaning
        unit.activate()
        self.assertEqual(unit.meaning, "Simbol")
        unit.display()


if __name__ == "__main__":
    unittest.main()

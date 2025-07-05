import unittest
from divine_agents.ontological_unit import OntologicalUnit


class TestOntologicalUnit(unittest.TestCase):
    def test_transition(self):
        unit = OntologicalUnit("ljubezen", "konotacija", "Močan občutek")
        unit.transition("Romantična ljubezen")
        self.assertEqual(unit.meaning, "Romantična ljubezen")


if __name__ == "__main__":
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.ontology import (
    OntologicalLibrary,
    DynamicOntologicalLibrary,
    PhilosophicalDebate,
)


class TestOntology(unittest.TestCase):
    def test_pridobi_nasprotje(self):
        library = OntologicalLibrary()
        self.assertEqual(library.pridobi_nasprotje("Veselje"), "Trpljenje")

    def test_interakcija_kontradikcija(self):
        library = DynamicOntologicalLibrary()
        res = library.interakcija("Veselje", "Trpljenje")
        self.assertIn("kontradikcijo", res)

    def test_philosophical_debate(self):
        library = DynamicOntologicalLibrary()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        debate = PhilosophicalDebate(a1, a2, library)
        lines = debate.debate("Veselje", "Trpljenje")
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

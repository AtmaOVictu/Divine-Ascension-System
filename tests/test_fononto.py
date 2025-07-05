import unittest
from divine_agents.fononto import FonontoTransition, OntologicalPhase


class TestFononto(unittest.TestCase):
    def test_apply_transition(self):
        tr = FonontoTransition("O", "T")
        meaning = tr.apply_transition()
        self.assertEqual(meaning, "Transformacija")

    def test_ontological_phase(self):
        phase = OntologicalPhase("Nova akcija", "Z", "A")
        result = phase.begin_phase()
        self.assertEqual(result, "Akcija, dejanje")


if __name__ == "__main__":
    unittest.main()

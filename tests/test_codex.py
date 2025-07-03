import unittest
from unittest.mock import patch

from divine_agents.codex import Codex


class TestCodex(unittest.TestCase):
    def test_generate_input(self):
        c = Codex()
        self.assertEqual(c.generate_input("Naloga"), "00 11 RESNICAMI: Naloga")

    def test_graph_edges(self):
        c = Codex()
        c.add_concept("A", "rdeca", "desc")
        c.add_concept("B", "modra", "desc")
        c.connect_concepts("A", "B")
        self.assertIn(("A", "B"), c.sozvocje.edges)

    def test_simulate_interaction_transition(self):
        c = Codex()
        a1 = c.add_agent("A1")
        a2 = c.add_agent("A2")
        with patch("random.sample", return_value=[a1, a2]):
            with patch("random.choice", return_value="strah"):
                msg = c.simulate_interaction()
        self.assertIn("strah", msg)
        self.assertEqual(a1.state, "Jaz")


if __name__ == "__main__":
    unittest.main()

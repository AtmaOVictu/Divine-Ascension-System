import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.generator import Generator


class TestGenerator(unittest.TestCase):
    def test_activation(self):
        g = Generator()
        g.aktiviraj()
        self.assertTrue(g.aktiviran)
        self.assertEqual(g.energija, 1.0)

    def test_generate_transitions(self):
        g = Generator()
        msg = g.generiraj_prehod("0")
        self.assertIn("ni aktiviran", msg)
        g.aktiviraj()
        msg = g.generiraj_prehod("0")
        self.assertIn("Prehod iz potencialnosti", msg)
        msg = g.generiraj_prehod("1")
        self.assertIn("Prehod v dejanskost", msg)
        msg = g.generiraj_prehod("⊘")
        self.assertIn("ustavi", msg)


if __name__ == "__main__":
    unittest.main()

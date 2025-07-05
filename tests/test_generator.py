import unittest
from divine_agents.generator import QuantityGenerator


class TestQuantityGenerator(unittest.TestCase):
    def test_high_tension(self):
        g = QuantityGenerator()
        g.transition(6)
        self.assertEqual(g.state, "Visoka napetost")

    def test_negation(self):
        g = QuantityGenerator()
        g.transition(-6)
        self.assertEqual(g.state, "Negacija")

    def test_stable(self):
        g = QuantityGenerator()
        g.transition(1)
        self.assertEqual(g.state, "Stabilno")


if __name__ == "__main__":
    unittest.main()

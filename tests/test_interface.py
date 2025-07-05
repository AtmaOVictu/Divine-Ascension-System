import unittest
from divine_agents.interface import Kapacitor


class TestKapacitor(unittest.TestCase):
    def test_state_transitions(self):
        k = Kapacitor()
        msg = k.sprejmi_vhod("aktiviraj")
        self.assertEqual(k.stanje, "Aktivacija")
        self.assertIn("aktivira", msg)
        msg = k.sprejmi_vhod("prehod")
        self.assertEqual(k.stanje, "Prehod")
        self.assertIn("uspešen", msg)
        msg = k.sprejmi_vhod("zaključi")
        self.assertEqual(k.stanje, "Zaključek")
        self.assertIn("zaključen", msg)


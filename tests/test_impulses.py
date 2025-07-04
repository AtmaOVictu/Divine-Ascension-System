import unittest
from divine_agents.impulses import Volja, Vera, Vzgib


class TestImpulses(unittest.TestCase):
    def test_volja_activation(self):
        v = Volja()
        self.assertEqual(v.state, 0)
        msg = v.aktivacija()
        self.assertEqual(v.state, 1)
        self.assertIn("aktivirana", msg)

    def test_vzgib_execution(self):
        vz = Vzgib()
        messages = vz.izvajanje()
        self.assertEqual(vz.volja.state, 1)
        self.assertEqual(vz.vera.state, 1)
        self.assertEqual(len(messages), 2)


if __name__ == '__main__':
    unittest.main()

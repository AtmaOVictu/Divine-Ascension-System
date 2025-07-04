import unittest
from divine_agents.curiosity import Radovednost


class TestCuriosity(unittest.TestCase):
    def test_cycle(self):
        r = Radovednost()
        self.assertEqual(r.state, "ne-zavedanje")
        r.aktiviraj()
        self.assertEqual(r.state, "iskanje")
        r.aktiviraj()
        self.assertEqual(r.state, "spoznanje")
        r.aktiviraj()
        self.assertEqual(r.state, "ne-zavedanje")


if __name__ == "__main__":
    unittest.main()

import unittest
from math import isclose

from divine_agents.transitions import biological_transition, social_transition


class TestTransitions(unittest.TestCase):
    def test_biological_halfway(self):
        self.assertTrue(isclose(biological_transition(0.5, 1.0, 0.5), 0.5, rel_tol=1e-6))

    def test_social_increasing(self):
        start = social_transition(0.4, 1.5, 0.6)
        end = social_transition(0.8, 1.5, 0.6)
        self.assertGreater(end, start)


if __name__ == "__main__":
    unittest.main()

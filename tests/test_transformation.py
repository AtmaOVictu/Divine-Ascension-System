import unittest
from divine_agents.transformation import (
    logistic_function,
    surreal_transition,
    DEFAULT_K_VALUES,
    DEFAULT_C_VALUES,
)


class TestSurrealTransition(unittest.TestCase):
    def test_logistic_function_bounds(self):
        value = logistic_function(0.5, 1.0, 0.5)
        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 1)

    def test_surreal_transition_sequence(self):
        states = surreal_transition(0.1)
        self.assertEqual(len(states), 9)
        for s in states:
            self.assertGreaterEqual(s, 0)
            self.assertLessEqual(s, 1)

    def test_surreal_transition_custom_params(self):
        k_values = [1.0] * 9
        c_values = [0.5] * 9
        states = surreal_transition(0.2, k_values, c_values)
        self.assertEqual(len(states), 9)


if __name__ == "__main__":
    unittest.main()

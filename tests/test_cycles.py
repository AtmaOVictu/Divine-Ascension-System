import unittest
from divine_agents.cycle import OuroborosCycle


class TestOuroborosCycle(unittest.TestCase):
    def test_cycle_sequence(self):
        cycle = OuroborosCycle()
        states = [cycle.cycle() for _ in range(3)]
        self.assertEqual(states, ["Jaz", "Enotnost", "Ego"])

    def test_run_cycles(self):
        cycle = OuroborosCycle(start_state="Jaz")
        history = cycle.run_cycles(2)
        self.assertEqual(history, ["Jaz", "Enotnost", "Ego"])


if __name__ == "__main__":
    unittest.main()

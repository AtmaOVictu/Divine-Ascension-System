import unittest
from divine_agents.agent import Agent
from divine_agents.gui import COLOR_MAP


class TestColorMap(unittest.TestCase):
    def test_all_states_mapped(self):
        for state in Agent.STATES:
            self.assertIn(state, COLOR_MAP)


if __name__ == "__main__":
    unittest.main()

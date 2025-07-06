import unittest
from divine_agents.granular import GranularAgent
from divine_agents.nano import NanoAgent


class TestGranularAgent(unittest.TestCase):
    def test_granular_transition_anger(self):
        agent = GranularAgent("G", emotions=["anger"], tension=0.8)
        state = agent.granular_transition()
        self.assertEqual(state, "Jaz")

    def test_granular_transition_calm(self):
        agent = GranularAgent("G", emotions=["calm"], tension=0.2)
        state = agent.granular_transition()
        self.assertEqual(state, "Enotnost")


class TestNanoAgent(unittest.TestCase):
    def test_execute_temperature(self):
        nano = NanoAgent("N", "analyze_temperature")
        self.assertEqual(nano.execute({"temperature": 30}), 36.0)

    def test_execute_pressure(self):
        nano = NanoAgent("N", "check_pressure")
        self.assertEqual(nano.execute({"pressure": 100}), 95.0)


if __name__ == "__main__":
    unittest.main()

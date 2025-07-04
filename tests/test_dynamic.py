import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.dynamic import (
    ExtrapolatingAgent,
    IntrospectiveAgent,
    SubstitutionAgent,
    Simulation,
    SpeculativeAgent,
    CodingSystem,
)


class TestDynamicAgents(unittest.TestCase):
    def test_extrapolating_encode(self):
        agent = ExtrapolatingAgent(1)
        result = agent.encode("abc")
        self.assertEqual(result, "bcd")

    def test_simulation_scenarios(self):
        sim = Simulation()
        scenarios = sim.generate_multiple_scenarios("ab", num=3)
        self.assertEqual(len(scenarios), 3)

    def test_speculative_length(self):
        spec = SpeculativeAgent()
        result = spec.speculate("ab")
        self.assertEqual(len(result), 2)

    def test_coding_system(self):
        system = CodingSystem(2)
        lines = system.process_data("abc")
        self.assertTrue(any("Simulacija" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

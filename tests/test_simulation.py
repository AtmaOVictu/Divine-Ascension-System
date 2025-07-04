import unittest
from divine_agents.simulation import (
    ExtrapolatingAgent,
    IntrospectiveAgent,
    SubstitutionAgent,
    Simulation,
    SpeculativeAgent,
)


class TestSimulationAgents(unittest.TestCase):
    def test_extrapolate(self):
        agent = ExtrapolatingAgent(1)
        self.assertEqual(agent.encode('ab'), 'bc')
        agent.encode('cd')
        self.assertNotIn('Ni dovolj', agent.extrapolate())

    def test_introspect(self):
        agent = IntrospectiveAgent(1)
        self.assertEqual(agent.encode('bc'), 'ab')
        agent.encode('de')
        self.assertNotIn('Ni dovolj', agent.introspect())

    def test_substitution(self):
        agent = SubstitutionAgent()
        out = agent.encode('aa')
        self.assertEqual(len(out), 2)
        self.assertTrue(out.isalpha())

    def test_simulation_and_speculation(self):
        sim = Simulation()
        future = sim.simulate_future('ab')
        self.assertEqual(len(future), 2)
        scenarios = sim.generate_multiple_scenarios('ab', num_scenarios=2)
        self.assertEqual(len(scenarios), 2)

        spec = SpeculativeAgent()
        spec_future = spec.speculate('ab')
        self.assertEqual(len(spec_future), 2)


if __name__ == '__main__':
    unittest.main()

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.bio_social import (
    biological_transition,
    social_transition,
    BioSocialAgent,
    simulate_agents,
)


class TestBioSocialTransitions(unittest.TestCase):
    def test_logistic_bounds(self):
        self.assertGreater(biological_transition(0.5, 1.0, 0.5), 0)
        self.assertLess(social_transition(0.0, 1.5, 0.6), 1)

    def test_agent_evolve(self):
        agent = BioSocialAgent("X")
        bio_before, soc_before = agent.get_bio_social_state()
        agent.evolve()
        bio_after, soc_after = agent.get_bio_social_state()
        self.assertNotEqual(bio_before, bio_after)
        self.assertNotEqual(soc_before, soc_after)

    def test_simulate_agents(self):
        agents = simulate_agents(3, 5)
        self.assertEqual(len(agents), 3)
        self.assertTrue(any(a.state in ("Jaz", "Enotnost") for a in agents))


if __name__ == "__main__":
    unittest.main()

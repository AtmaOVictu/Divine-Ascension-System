import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.multi_agent import BioSocialAgent, create_random_agents


class TestMultiAgent(unittest.TestCase):
    def test_evolve_bounds(self):
        agent = BioSocialAgent(k_bio=1.0, c_bio=0.5, k_soc=1.5, c_soc=0.6)
        before = agent.get_state()
        agent.evolve()
        after = agent.get_state()
        for val in after:
            self.assertGreaterEqual(val, 0.0)
            self.assertLessEqual(val, 1.0)
        self.assertNotEqual(before, after)

    def test_create_random_agents(self):
        agents = create_random_agents(5)
        self.assertEqual(len(agents), 5)
        for ag in agents:
            self.assertIsInstance(ag, BioSocialAgent)


if __name__ == "__main__":
    unittest.main()

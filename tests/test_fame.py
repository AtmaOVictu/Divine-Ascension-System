import unittest
from divine_agents.agent import Agent, fame_tiers, social_influence


class TestFameSystem(unittest.TestCase):
    def test_fame_update_range(self):
        agent = Agent("A")
        fame = agent.update_fame(0.3, 0.1, 0.7)
        self.assertGreaterEqual(fame, 0.0)
        self.assertLessEqual(fame, 1.0)

    def test_fame_decay(self):
        agent = Agent("A")
        agent.fame = 1.0
        agent.apply_fame_decay()
        self.assertLess(agent.fame, 1.0)
        self.assertGreaterEqual(agent.fame, 0.0)

    def test_social_influence(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        a1.fame = 0.9
        a2.fame = 0.5
        self.assertTrue(social_influence(a1, a2))
        a2.fame = 0.95
        self.assertFalse(social_influence(a1, a2))

    def test_fame_tiers(self):
        agent = Agent("A")
        agent.fame = 0.85
        self.assertEqual(fame_tiers(agent), "Legendary")


if __name__ == "__main__":
    unittest.main()

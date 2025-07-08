import unittest
from divine_agents import Agent, ReputationSystem


class TestFameSystem(unittest.TestCase):
    def test_fame_decay(self):
        agent = Agent("A")
        agent.update_fame(positive_actions=2, negative_actions=0, participation_score=5)
        fame_before = agent.fame
        agent.apply_fame_decay()
        self.assertLess(agent.fame, fame_before)

    def test_help_interaction(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        rep = ReputationSystem()
        rep.interact(a1, a2, action="help")
        self.assertGreater(a1.fame, 0)
        self.assertGreater(a2.fame, 0)

    def test_fame_tier(self):
        agent = Agent("A")
        agent.update_fame(positive_actions=10, negative_actions=0, participation_score=10)
        self.assertIn(agent.fame_tier(), ["Unknown", "Moderate Fame", "Influential", "Legendary"])


if __name__ == '__main__':
    unittest.main()

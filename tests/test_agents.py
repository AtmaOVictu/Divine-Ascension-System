import unittest
from divine_agents.agent import Agent, fame_tiers, social_influence
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_fame_update_and_tiers(self):
        agent = Agent("F")
        fame = agent.update_fame(0.3, 0.1, 0.7)
        self.assertGreaterEqual(fame, 0.0)
        self.assertLessEqual(fame, 1.0)
        tier = fame_tiers(agent)
        self.assertIn(tier, ["Unknown", "Moderate Fame", "Influential", "Legendary"])

    def test_social_influence(self):
        a1 = Agent("A1", fame=0.8)
        a2 = Agent("A2", fame=0.2)
        self.assertTrue(social_influence(a1, a2))


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent, fame_tier
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

    def test_fame_update_and_tier(self):
        agent = Agent("F")
        agent.update_fame(0.4, 0.1, 0.5)
        self.assertGreaterEqual(agent.fame, 0.0)
        self.assertLessEqual(agent.fame, 1.0)
        tier = fame_tier(agent)
        self.assertIn(tier, ["Unknown", "Moderate Fame", "Influential", "Legendary"])


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.reputation import ReputationSystem


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

    def test_fame_update_and_decay(self):
        agent = Agent("F")
        agent.update_fame(positive_actions=3)
        initial_fame = agent.fame
        self.assertGreater(initial_fame, 0)
        # Apply only decay to ensure fame decreases
        agent.apply_fame_decay()
        self.assertLess(agent.fame, initial_fame)

    def test_fame_tier(self):
        agent = Agent("T")
        agent.fame = 55
        self.assertEqual(agent.fame_tier(), "Influential")

    def test_reputation_interaction(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        rep = ReputationSystem()
        rep.interact(a1, a2, action="help")
        self.assertGreater(a1.fame, 0)
        self.assertGreater(a2.fame, 0)


if __name__ == '__main__':
    unittest.main()

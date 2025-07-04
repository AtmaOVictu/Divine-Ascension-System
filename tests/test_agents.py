import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        agent.update_emotion(0.6, "joy")
        self.assertEqual(agent.transition(), "Enotnost")

    def test_response_prefix(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "anger")
        agent.transition()
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z jezo"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Dialogue should mention Enotnost after transitions
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

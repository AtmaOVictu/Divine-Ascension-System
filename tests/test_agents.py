import unittest
from divine_agents.agent import Agent, EmotionType
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, EmotionType.ANGER)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_with_emotion(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.4, EmotionType.JOY)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue, agent2 should reach Enotnost state
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

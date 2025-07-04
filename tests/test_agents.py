import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        self.assertEqual(agent.tension_threshold, Agent.TENSION_THRESHOLD)
        self.assertEqual(agent.emotion_threshold, Agent.EMOTION_THRESHOLD)
        agent.update_tension(Agent.TENSION_THRESHOLD + 0.1)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_custom_threshold_override(self):
        agent = Agent("B", tension_threshold=0.3, emotion_threshold=0.2)
        agent.update_emotion(0.25)
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


if __name__ == '__main__':
    unittest.main()

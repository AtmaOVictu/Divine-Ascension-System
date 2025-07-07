import unittest
from divine_agents.agent import Agent, Emotion
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

    def test_emotion_driven_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(Emotion.FEAR, 0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_emotional_response_prefix(self):
        agent = Agent("C")
        agent.update_emotion(Emotion.ANGER, 0.6)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("Anger", response.capitalize())


if __name__ == '__main__':
    unittest.main()

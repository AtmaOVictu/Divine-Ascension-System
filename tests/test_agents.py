import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_mood_influence(self):
        agent = Agent("C")
        calm_reply = agent.respond("Kaj je resnica?")
        agent.update_emotion(0.9, mood="angry")
        angry_reply = agent.respond("Kaj je resnica?")
        self.assertTrue(angry_reply.isupper())
        self.assertNotEqual(calm_reply, angry_reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion_mods=(0.8, 0.6))
        self.assertTrue(all(isinstance(l, tuple) for l in lines))
        self.assertTrue(any("Enotnost" in text for _, text in lines))


if __name__ == '__main__':
    unittest.main()

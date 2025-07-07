import unittest
from divine_agents.agent import Agent
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

    def test_transition_emotion_only(self):
        agent = Agent("B")
        agent.emotion = 0.6  # exceed emotion threshold without affecting tension
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.tension, 0.0)

    def test_respond_emotional_states(self):
        agent = Agent("C")
        agent.emotion = 0.8
        high = agent.respond("Kaj je resnica?")
        agent.emotion = 0.2
        low = agent.respond("Kaj je resnica?")
        self.assertIn("vznemirjeno", high)
        self.assertIn("mirno", low)

    def test_dialogue_with_emotions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.3, emotion2=0.9)
        # a1 should not transition, a2 should move to Enotnost
        self.assertIn("A1 (Ego)", lines[0])
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

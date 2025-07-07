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

    def test_emotion_driven_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("C")
        agent.update_emotion(0.3, "veselje")
        # Emotion label should be hidden by default
        hidden_response = agent.respond("Kaj je resnica?")
        self.assertNotIn("veselje", hidden_response)

        # Reveal emotion when explicitly requested
        response = agent.respond("Kaj je resnica?", reveal_emotion=True)
        self.assertIn("veselje", response)

    def test_reveal_emotion_label(self):
        agent = Agent("D")
        agent.update_emotion(0.9, "jeza")
        label = agent.get_emotion_label()
        self.assertEqual(label["type"], "jeza")
        self.assertTrue(label["hidden"])


if __name__ == '__main__':
    unittest.main()

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

    def test_negative_emotion(self):
        agent = Agent("A")
        with self.assertRaises(ValueError):
            agent.update_emotion(-0.1)

    def test_emotion_clamping(self):
        agent = Agent("A", tension=0.5)
        agent.update_emotion(0.8)
        self.assertLessEqual(agent.tension, 1.0)

    def test_emotion_tone_in_response(self):
        agent = Agent("A", emotion=0.8)
        self.assertIn("Moja", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

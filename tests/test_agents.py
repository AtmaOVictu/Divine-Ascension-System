import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_updates_mood(self):
        agent = Agent("A")
        agent.update_emotion(0.9, mood="strah")
        self.assertEqual(agent.mood, "strah")
        self.assertGreater(agent.tension, 0.0)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_response_emotional(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion(0.6, mood="jeza")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("jeza", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("jeza" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

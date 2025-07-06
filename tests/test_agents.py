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

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.5)
        agent.update_emotion(0.1)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_express_emotion_updates_tension(self):
        agent = Agent("C")
        agent.express_emotion("fear")
        self.assertAlmostEqual(agent.emotion, Agent.EMOTION_VALUES["fear"])
        self.assertGreater(agent.tension, 0)

    def test_dialogue_triggers_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = philosophical_dialogue(a1, a2)
        transitioned = any("prehaja v stanje" in l for l in lines)
        self.assertTrue(transitioned)


if __name__ == '__main__':
    unittest.main()

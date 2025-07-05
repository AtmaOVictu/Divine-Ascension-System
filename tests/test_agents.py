import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_parameters(self):
        scenarios = [
            ("Ego", 0.8, 0.0, "Jaz"),
            ("Ego", 0.0, 0.6, "Jaz"),
            ("Jaz", 0.8, 0.0, "Enotnost"),
            ("Jaz", 0.0, 0.6, "Enotnost"),
            ("Ego", 0.7, 0.0, "Ego"),
            ("Ego", 0.0, 0.5, "Ego"),
        ]
        for start, tension, emotion, expected in scenarios:
            with self.subTest(start=start, tension=tension, emotion=emotion):
                agent = Agent("A", state=start)
                agent.update_tension(tension)
                agent.update_emotion(emotion)
                state = agent.transition()
                self.assertEqual(state, expected)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestAgentUpdates(unittest.TestCase):
    def test_update_emotion_alters_tension(self):
        agent = Agent("A")
        agent.update_emotion(0.4)
        self.assertEqual(agent.emotion, 0.4)
        self.assertEqual(agent.tension, 0.4)

    def test_update_tension_sets_value(self):
        agent = Agent("A")
        agent.update_tension(0.6)
        self.assertEqual(agent.tension, 0.6)


class TestStateHistory(unittest.TestCase):
    def test_history_records_states(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()

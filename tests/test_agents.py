import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("čustvo", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_tracking(self):
        agent = Agent("A")
        agent.update_emotion("joy", 0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_emotion_increases_tension(self):
        agent = Agent("A")
        agent.update_emotion("anger", 0.3)
        self.assertGreater(agent.tension, 0.0)


if __name__ == '__main__':
    unittest.main()

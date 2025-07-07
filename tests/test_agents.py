import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_emotion("joy", 0.4)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertEqual(len(agent.history), 2)

    def test_emotion_increases_tension(self):
        agent = Agent("C")
        start_tension = agent.tension
        agent.update_emotion("anger", 0.6)
        self.assertGreater(agent.tension, start_tension)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion("joy", 0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("Čutim", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

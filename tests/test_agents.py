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

    def test_emotion_triggers_transition(self):
        agent = Agent("A", tension=0.3)
        agent.update_emotion(0.5, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_joy_reduces_tension(self):
        agent = Agent("A", tension=0.8)
        agent.update_emotion(0.5, "joy")
        self.assertLess(agent.tension, 0.8)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

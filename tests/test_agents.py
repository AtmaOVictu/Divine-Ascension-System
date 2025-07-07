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

    def test_emotion_based_transition(self):
        agent = Agent("A")
        agent.set_emotion("joy")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_influenced_response(self):
        agent = Agent("A")
        agent.set_emotion("fear")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("S strahom", reply)

    def test_multiple_emotion_transitions(self):
        agent = Agent("A")
        agent.set_emotion("joy")
        agent.update_emotion(0.9)
        state_after_joy = agent.transition()
        self.assertEqual(state_after_joy, "Jaz")

        agent.set_emotion("fear")
        agent.update_emotion(0.7)
        state_after_fear = agent.transition()
        self.assertEqual(state_after_fear, "Enotnost")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, emotion_type="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_include_emotion(self):
        agent = Agent("C", state="Enotnost")
        agent.update_emotion(0.4, emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure at least one transition occurs in the dialogue
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

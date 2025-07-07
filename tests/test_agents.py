import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # emotion alone should also trigger a transition
        agent2 = Agent("B")
        agent2.update_emotion(0.6, "fear")
        state2 = agent2.transition()
        self.assertEqual(state2, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="mir")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("mir", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Verify that at least one agent reaches the state "Enotnost"
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Emotion descriptors should be part of the dialogue
        self.assertTrue(any("jeza" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

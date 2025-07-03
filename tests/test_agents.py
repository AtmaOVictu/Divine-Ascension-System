import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # transition via emotion
        agent2 = Agent("B")
        agent2.update_emotion(0.6, emotion_type="fear")
        state2 = agent2.transition()
        self.assertEqual(state2, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        agent.update_emotion(0.3, emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Vse resnice", reply)
        self.assertIn("radostjo", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # after dialogue one agent should mention Enotnost or Jaz depending on transition
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

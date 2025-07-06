import unittest
from divine_agents import Agent, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6, emotion_type="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("vesel", reply.lower())

    def test_dialogue(self):
        a1 = Agent("A1", emotion_type="fear")
        a2 = Agent("A2", state="Jaz", emotion_type="joy")
        lines = philosophical_dialogue(a1, a2, turns=2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

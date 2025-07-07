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
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))

    def test_emotion_from_shadows(self):
        agent = Agent("A", shadows={"past": 0.6})
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_connection(self):
        a1 = Agent("A1", emotion=1.0)
        a2 = Agent("A2", emotion=0.0)
        a1.connect(a2)
        a1.share_emotion()
        self.assertAlmostEqual(a1.emotion, a2.emotion)


if __name__ == '__main__':
    unittest.main()

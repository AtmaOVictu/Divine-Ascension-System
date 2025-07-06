import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response_prefix(self):
        agent = Agent("C", emotion=0.8, emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z veseljem"))

    def test_dialogue(self):
        a1 = Agent("A1", emotion_type="fear")
        a2 = Agent("A2", state="Jaz", emotion_type="joy")
        lines = philosophical_dialogue(a1, a2, turns=2)
        self.assertTrue(a1.state in ("Jaz", "Enotnost"))
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

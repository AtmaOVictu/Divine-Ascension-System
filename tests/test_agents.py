import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggered_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response(self):
        agent = Agent("C")
        agent.update_emotion(0.4, "joy")
        text = agent.respond("Kaj je resnica?")
        self.assertIn("veseljem", text)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Check that emotional prefixes are present
        self.assertTrue(any("jezo" in line or "veseljem" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

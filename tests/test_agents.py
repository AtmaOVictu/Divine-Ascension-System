import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_without_threshold(self):
        agent = Agent("A")
        agent.update_emotion(0.4)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response(self):
        agent = Agent("B", emotion_type="anger")
        agent.update_emotion(0.9)
        text = agent.respond("Kaj je resnica?")
        self.assertIn("jezo", text)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Ensure emotional phrases are present
        self.assertTrue(any("jezo" in line or "radost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

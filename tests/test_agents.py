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
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_when_below_thresholds(self):
        agent = Agent("C")
        agent.update_tension(0.3)
        agent.update_emotion(0.4, "joy")
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion(0.5, "anger")
        response = agent.respond("Kaj je resnica?")
        self.assertTrue(response.startswith("V jezi"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Ensure emotional context is present
        self.assertTrue(any("jezi" in line or "radosti" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

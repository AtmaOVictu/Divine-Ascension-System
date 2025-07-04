import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("A")
        agent.update_emotion(0.2, "mir")
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response(self):
        agent = Agent("B", state="Ego")
        agent.update_emotion(0.6, "strah")
        agent.transition()
        response = agent.respond("Kaj je resnica?")
        self.assertIn("strah", response)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue, at least one agent should be in a new state
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        # Responses should mention emotions
        self.assertTrue(any("Moje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

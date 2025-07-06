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
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.apply_emotion("strah", 0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_response(self):
        agent = Agent("C", state="Ego")
        agent.apply_emotion("veselje", 0.7)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", response)


if __name__ == '__main__':
    unittest.main()

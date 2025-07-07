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
        self.assertIn("eno", reply.lower())

    def test_emotional_response(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        response = agent.respond("Kaj je resnica?")
        self.assertTrue(response.isupper())

    def test_dialogue_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("Enotnost", " ".join(lines))
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()

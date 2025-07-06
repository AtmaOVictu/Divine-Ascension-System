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

    def test_environment_transition(self):
        agent = Agent("Env", environment="disharmonious")
        agent.simulate_environment()
        self.assertIn(agent.state, Agent.STATES)
        self.assertGreaterEqual(agent.emotion, 0.7)
        self.assertEqual(agent.state, "Jaz")

    def test_emotional_response_prefix(self):
        agent = Agent("Emo")
        agent.update_emotion(0.8)
        response = agent.respond("Kaj je resnica?")
        self.assertTrue(response.startswith("Intenzivno"))

    def test_dialogue(self):
        a1 = Agent("A1", environment="disharmonious")
        a2 = Agent("A2", state="Jaz", environment="disharmonious")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

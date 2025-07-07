import unittest
from divine_agents.agent import Agent


class TestSelfAwareness(unittest.TestCase):
    def test_emotional_transition(self):
        agent = Agent("Agent1")
        agent.update_emotion("joy")
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        self.assertTrue(any("Transitioned to Jaz" in log for log in agent.logs))

    def test_emotional_response(self):
        agent = Agent("Agent2", state="Jaz")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", response)
        self.assertTrue(any("Responded with" in log for log in agent.logs))

if __name__ == "__main__":
    unittest.main()

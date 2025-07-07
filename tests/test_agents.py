import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestSelfAwareness(unittest.TestCase):
    def test_emotional_transition(self):
        agent = Agent("Agent1", emotion="joy")
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        self.assertTrue(any("transitioned to Jaz" in log for log in agent.logs))

    def test_emotional_response(self):
        agent = Agent("Agent2", state="Jaz", emotion="anger")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("anger", reply)

    def test_update_emotion(self):
        agent = Agent("Agent3", emotion="fear")
        agent.update_emotion("joy")
        self.assertEqual(agent.emotion, "joy")
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

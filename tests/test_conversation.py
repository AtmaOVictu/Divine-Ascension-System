import unittest
from divine_agents import Agent, philosophical_debate


class TestConversation(unittest.TestCase):
    def test_emotion_transition(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Enotnost")

    def test_emotional_response(self):
        agent = Agent("A", emotion=0.7)
        response = agent.respond("Kaj je resnica?")
        self.assertTrue(response.startswith("Čustveno menim"))

    def test_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()

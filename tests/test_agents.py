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
        self.assertIn("fearful", reply)

    def test_emotional_responses(self):
        agent = Agent("A")
        agent.update_emotion(0.2)
        resp1 = agent.respond("Kaj je resnica?")
        agent.update_emotion(0.5)
        resp2 = agent.respond("Kaj je resnica?")
        agent.update_emotion(0.9)
        resp3 = agent.respond("Kaj je resnica?")
        self.assertIn("fearful", resp1)
        self.assertIn("joyful", resp2)
        self.assertIn("angry", resp3)
        self.assertNotEqual(resp1, resp2)
        self.assertNotEqual(resp2, resp3)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

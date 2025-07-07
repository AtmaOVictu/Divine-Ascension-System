import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion("joy", 0.4)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("veseljem", reply.lower())

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

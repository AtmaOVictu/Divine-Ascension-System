import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent2 = Agent("B")
        agent2.express_emotion("fear", 0.6)
        state2 = agent2.transition()
        self.assertEqual(state2, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.express_emotion("joy", 0.4)
        reply_with_emotion = agent.respond("Kaj je resnica?")
        self.assertIn("joy", reply_with_emotion)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, ("anger", 0.9), ("joy", 0.7))
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Čustvo" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

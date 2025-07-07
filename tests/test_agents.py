import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        self.assertIn("Z veliko strastjo", agent.respond("Kaj je resnica?"))

        agent.update_emotion(0.5)
        self.assertIn("Mirno razlagam", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(len(lines), 6)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()

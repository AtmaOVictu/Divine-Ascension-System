import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Ego")
        self.assertIn("absolutna", agent.respond("?"))

        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("?"))

        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(a1.state == "Enotnost" or a2.state == "Enotnost")
        self.assertGreater(len(lines), 0)


if __name__ == '__main__':
    unittest.main()

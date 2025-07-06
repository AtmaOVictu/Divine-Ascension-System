import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_responses(self):
        agent = Agent("A")
        self.assertIn("absolutna", agent.respond("Kaj je resnica?"))

        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("Kaj je resnica?"))

        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(len(lines) > 0)


if __name__ == '__main__':
    unittest.main()

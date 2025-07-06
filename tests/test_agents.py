import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.6)
        self.assertEqual(agent.transition(), "Ego")

        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.2)
        reply_calm = agent.respond("Kaj je resnica?")
        self.assertIn("mirno", reply_calm)

        agent.update_emotion(0.9)
        reply_emotional = agent.respond("Kaj je resnica?")
        self.assertIn("čustveno", reply_emotional)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("čustveno" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

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
        agent2.update_emotion(0.6, "strah")
        state2 = agent2.transition()
        self.assertEqual(state2, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.4, "veselje")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("veselje", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Agent1 should transition to Jaz and agent2 to Enotnost
        self.assertIn("Jaz", lines[2])
        self.assertIn("Enotnost", lines[3])


if __name__ == '__main__':
    unittest.main()

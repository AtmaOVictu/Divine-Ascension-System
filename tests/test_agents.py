import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.update_emotion(0.1)
        # dynamic_tension remains below threshold, emotion below threshold
        self.assertEqual(agent.transition(), "Ego")

        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_calculate_tension(self):
        agent = Agent("B", tension=0.5, emotion=0.6)
        expected = (0.6 ** 2) / (1 + 0.5)
        self.assertAlmostEqual(agent.calculate_tension(), expected)

    def test_transition_with_emotion(self):
        agent = Agent("C", tension=0.3, emotion=0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

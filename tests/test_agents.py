import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_emotion_only(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_border_thresholds(self):
        agent = Agent("C")
        agent.update_tension(0.7)
        self.assertEqual(agent.transition(), "Ego")
        agent.update_tension(0)
        agent.update_emotion(0.5)
        self.assertEqual(agent.transition(), "Ego")

    def test_history(self):
        agent = Agent("D")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

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

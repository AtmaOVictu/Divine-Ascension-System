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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_multiple_transitions(self):
        agent = Agent("Hist")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.9)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_emotion_thresholds(self):
        high_emotion_agent = Agent("Em")
        high_emotion_agent.update_emotion(0.9)
        state = high_emotion_agent.transition()
        self.assertEqual(state, "Jaz")

        low_agent = Agent("Low")
        low_agent.update_tension(0.3)
        low_agent.update_emotion(0.4)
        state_low = low_agent.transition()
        self.assertEqual(state_low, "Ego")

    def test_dialogue_state_updates(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("prehaja v stanje: Jaz", lines[2])
        self.assertIn("prehaja v stanje: Enotnost", lines[3])
        self.assertIn("relativna", lines[4])
        self.assertIn("eno", lines[5])


if __name__ == '__main__':
    unittest.main()

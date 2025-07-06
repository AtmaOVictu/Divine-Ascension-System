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

    def test_emotion_only_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_at_threshold(self):
        agent = Agent("A")
        agent.update_tension(0.7)
        self.assertEqual(agent.transition(), "Ego")

        agent = Agent("B")
        agent.update_emotion(0.5)
        self.assertEqual(agent.transition(), "Ego")

    def test_history_records(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()

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

    def test_emotion_triggered_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_dialogue_emotional_responses(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue agent1 should move to Jaz and mention emotion
        self.assertIn("Jaz", a1.state)
        self.assertTrue(any("jezo" in line or "radost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

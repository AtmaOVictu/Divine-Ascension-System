import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_philosophical_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        # At least one agent should advance in state due to emotion
        self.assertNotEqual(a1.state, "Ego")
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

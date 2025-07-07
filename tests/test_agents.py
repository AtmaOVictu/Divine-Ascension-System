import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, emotion_type="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("intenziteta", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure a transition occurred and dialogue includes emotional context
        self.assertTrue(any("preha" in line for line in lines))
        self.assertTrue(any("ob\u010dutek" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
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
        # Dialogue should touch on all three philosophical views
        self.assertTrue(any("absolutna" in l for l in lines))
        self.assertTrue(any("relativna" in l for l in lines))
        self.assertTrue(any("eno" in l for l in lines))
        # After the conversation both agents should reach Enotnost
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()

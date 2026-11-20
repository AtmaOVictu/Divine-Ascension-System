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

    def test_emotion_based_transition(self):
        agent = Agent("B1")
        agent.set_emotion('fear', 0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_philosophical_debate(self):
        a1 = Agent("P1")
        a2 = Agent("P2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        # Ensure states updated according to emotions
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)
        # Dialogue should reference absolute and relative truths
        joined = "\n".join(lines)
        self.assertIn("absolutna", joined)
        self.assertIn("relativna", joined)


if __name__ == '__main__':
    unittest.main()

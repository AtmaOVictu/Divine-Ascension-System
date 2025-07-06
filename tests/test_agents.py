import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_tension_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, label="fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.update_emotion(0.7, label="joy")
        self.assertIn("veseljem", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure at least one agent reaches Enotnost during the dialogue
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Dialogue should produce multiple lines reflecting both agents
        self.assertGreaterEqual(len(lines), 4)


if __name__ == '__main__':
    unittest.main()

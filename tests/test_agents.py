import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # Transition triggered by tension
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        agent = Agent("B")
        # Transition triggered by emotion
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_type="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("ob\u010dutek", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Dialogue should contain state transitions
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

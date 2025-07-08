import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        # below threshold
        agent.update_tension(0.5)
        self.assertEqual(agent.transition(), "Ego")

        # above threshold via tension
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        # second transition triggered by emotion
        agent.update_emotion(0.6, "joy")
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure emotions and transitions are mentioned in the dialogue
        self.assertTrue(any("čuti" in l for l in lines))
        self.assertTrue(any("prehaja v stanje" in l for l in lines))


if __name__ == '__main__':
    unittest.main()

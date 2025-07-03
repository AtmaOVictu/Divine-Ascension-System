import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestExtendedDialogue(unittest.TestCase):
    def test_emotion_trigger_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.9, "fear")
        self.assertEqual(agent.transition(), "Jaz")
        self.assertEqual(agent.emotion_label, "fear")

    def test_emotional_response(self):
        agent = Agent("B", state="Ego", emotion_label="anger")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("absolutna", response)
        self.assertIn("jezo", response)

    def test_dialogue_content(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After dialogue agent1 should have transitioned to Jaz
        self.assertIn("Jaz", a1.history[-1])
        # There should be emotional prefixes in the lines
        self.assertTrue(any("z jezo".lower() in line.lower() for line in lines))


if __name__ == "__main__":
    unittest.main()

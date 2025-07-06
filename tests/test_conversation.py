import unittest
from divine_agents import Agent, emotional_dialogue


class TestEmotionalDialogue(unittest.TestCase):
    def test_emotion_triggered_transition(self):
        agent = Agent("X")
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_dialogue_content(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2)
        # Ensure philosophical statements are present
        self.assertTrue(any("Resnica" in line for line in lines))
        # Ensure state transitions occurred
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

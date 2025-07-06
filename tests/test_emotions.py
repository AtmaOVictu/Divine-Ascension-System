import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import emotional_dialogue


class TestEmotionalBehaviour(unittest.TestCase):
    def test_emotion_trigger_transition(self):
        agent = Agent("X")
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_dialogue_prefixes(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2)
        joined = " ".join(lines)
        self.assertIn("Z jezo", joined)
        self.assertIn("V strahu", joined)
        self.assertIn("Enotnost", joined)


if __name__ == "__main__":
    unittest.main()

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.emotional_agent import EmotionalAgent
from divine_agents.dialogue import emotional_dialogue


class TestEmotionalAgent(unittest.TestCase):
    def test_color_mapping_and_transition(self):
        agent = EmotionalAgent("E")
        agent.update_emotion(0.6, "anger")
        self.assertEqual(agent.transition(), "Jaz")
        self.assertIn("red", agent.describe_emotion())

    def test_emotional_dialogue(self):
        a1 = EmotionalAgent("A1")
        a2 = EmotionalAgent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2)
        # ensure unified state eventually appears
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("red" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

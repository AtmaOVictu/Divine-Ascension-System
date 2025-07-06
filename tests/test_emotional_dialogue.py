import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import emotional_dialogue


class TestEmotionalDialogue(unittest.TestCase):
    def test_emotional_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = emotional_dialogue(a1, a2)
        # A1 should transition from Ego to Jaz because emotion 0.6 > 0.5
        self.assertIn("Jaz", a1.history)
        # A2 should transition from Ego to Jaz due to tension 0.8 > 0.7
        self.assertIn("Jaz", a2.history)
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import emotional_dialogue


class TestEmotionalDialogue(unittest.TestCase):
    def test_emotional_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2, rounds=2, emotions1=["fear", "anger"], emotions2=["joy", "sorrow"])
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

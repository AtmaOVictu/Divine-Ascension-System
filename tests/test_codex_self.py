import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.codex_self import CodexSelf, EmotionalDialogue


class TestCodexSelf(unittest.TestCase):
    def test_emotional_transition(self):
        codex = CodexSelf("OntoCodex")
        outputs = codex.emotional_transition("joy")
        self.assertIn("joy", outputs[0])
        self.assertIn("idself", outputs[1])

    def test_dialogue_anger(self):
        codex = EmotionalDialogue("EmoCodex")
        codex.emotional_transition("anger")
        line = codex.start_dialogue("The meaning of life")
        self.assertIn("intensity", line)


if __name__ == "__main__":
    unittest.main()

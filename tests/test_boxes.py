import unittest
from divine_agents import Agent, SymbolicBox, EmotionalBox, EmotionalAgent, threshold_dialogue


class TestSymbolicBox(unittest.TestCase):
    def test_valid_transition(self):
        box = SymbolicBox(stage="∴")
        self.assertTrue(box.is_valid_transition("∆"))
        box.transition("∆", {"status": "processing"})
        self.assertEqual(box.stage, "∆")
        self.assertEqual(box.get_data()["status"], "processing")


class TestEmotionalBox(unittest.TestCase):
    def test_negative_emotion_blocks(self):
        e_agent = EmotionalAgent("EA")
        ebox = EmotionalBox("anger")
        status = ebox.process_emotion(e_agent)
        self.assertEqual(status, "Emotion confirmed: Negative")
        result = ebox.transition_emotion(e_agent)
        self.assertEqual(result, "Emotion halted. Task cannot proceed.")


class TestThresholdDialogue(unittest.TestCase):
    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = threshold_dialogue(a1, a2)
        self.assertTrue(any("Box at stage" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

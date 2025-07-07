import unittest
from divine_agents.emotion import EmotionalAgent, EmotionalBox, MainTaskAgent


class TestEmotionalFlow(unittest.TestCase):
    def test_emotional_agent_positive(self):
        agent = EmotionalAgent()
        box = EmotionalBox("joy")
        status = box.process(agent)
        self.assertEqual(status, "Emotion confirmed: Positive")

    def test_main_task_negative(self):
        main = MainTaskAgent("Main")
        box = EmotionalBox("anger")
        result = main.handle_task("Analyze", box)
        self.assertIn("halted", result)
        self.assertEqual(main.state, "Jaz")

    def test_main_task_transition(self):
        main = MainTaskAgent("Main")
        box = EmotionalBox("happiness")
        result = main.handle_task("Analyze", box)
        self.assertIn("completed", result)
        self.assertEqual(main.state, "Jaz")


if __name__ == "__main__":
    unittest.main()

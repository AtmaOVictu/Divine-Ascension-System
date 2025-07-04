import unittest
from divine_agents.body_soul_spirit import BodyAgent, SoulAgent, SpiritAgent


class TestBodySoulSpiritAgents(unittest.TestCase):
    def test_body_transitions(self):
        body = BodyAgent()
        body.transition("Sensation")
        self.assertEqual(body.get_state(), "Sensation")
        body.transition("Action")
        self.assertEqual(body.get_state(), "Action")

    def test_soul_transitions(self):
        soul = SoulAgent()
        soul.transition("Emotion")
        self.assertEqual(soul.get_state(), "Emotion")
        soul.transition("Reflection")
        self.assertEqual(soul.get_state(), "Reflection")

    def test_spirit_transitions(self):
        spirit = SpiritAgent()
        spirit.transition("Unity")
        self.assertEqual(spirit.get_state(), "Unity")
        spirit.transition("Eternal")
        self.assertEqual(spirit.get_state(), "Eternal")


if __name__ == "__main__":
    unittest.main()

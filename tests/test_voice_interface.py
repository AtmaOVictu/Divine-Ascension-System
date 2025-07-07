import unittest

from divine_agents.voice_interface import (
    speech_to_text,
    text_to_speech,
    VoiceAgent,
    ConversationalSystem,
)


class TestVoiceInterface(unittest.TestCase):
    def test_speech_to_text(self):
        self.assertEqual(speech_to_text(" hello "), "hello")

    def test_text_to_speech(self):
        audio = text_to_speech("hi")
        self.assertIn("hi", audio)

    def test_conversational_step(self):
        agent1 = VoiceAgent("A1")
        agent2 = VoiceAgent("A2", state="Jaz")
        system = ConversationalSystem(agent1, agent2)
        text, audio = system.step("fear is powerful")
        self.assertIn("Audio", audio)
        self.assertIn(agent1.state, ["Jaz", "Enotnost"])
        self.assertTrue(text.startswith("fear"))


if __name__ == "__main__":
    unittest.main()

"""Voice interface utilities combining STT, TTS, and realtime handling."""
from typing import Tuple

from .agent import Agent


def speech_to_text(audio_input: str) -> str:
    """Simulate speech-to-text by returning the provided audio input."""
    # In a real application, audio data would be processed here.
    return audio_input.strip()


def text_to_speech(text: str) -> str:
    """Simulate text-to-speech by returning an audio placeholder."""
    # In a real application, this would produce audio output.
    return f"Audio: {text}"


class VoiceAgent(Agent):
    """Agent with simple STT/TTS capabilities."""

    def hear(self, audio_input: str) -> str:
        """Process audio input and update emotion based on keywords."""
        text = speech_to_text(audio_input)
        if "fear" in text or "strah" in text:
            self.update_emotion(0.8)
        elif "anger" in text or "jeza" in text:
            self.update_emotion(0.9)
        elif "joy" in text or "veselje" in text:
            self.update_emotion(0.6)
        else:
            self.update_emotion(0.1)
        self.transition()
        return text

    def speak(self, prompt: str) -> str:
        response = self.respond(prompt)
        return text_to_speech(response)


class ConversationalSystem:
    """Simple system demonstrating combined STT and TTS usage."""

    def __init__(self, agent1: VoiceAgent, agent2: VoiceAgent):
        self.agent1 = agent1
        self.agent2 = agent2

    def step(self, audio_input: str) -> Tuple[str, str]:
        """Run one conversational step and return text and audio outputs."""
        text = self.agent1.hear(audio_input)
        audio_response = self.agent2.speak(text)
        return text, audio_response

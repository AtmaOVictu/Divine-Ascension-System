from .agent import Agent
from .dialogue import philosophical_dialogue
from .voice_interface import (
    speech_to_text,
    text_to_speech,
    VoiceAgent,
    ConversationalSystem,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "speech_to_text",
    "text_to_speech",
    "VoiceAgent",
    "ConversationalSystem",
]

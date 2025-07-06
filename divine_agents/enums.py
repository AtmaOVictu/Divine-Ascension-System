from enum import Enum

class State(Enum):
    """Ontological states an agent can inhabit."""
    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"

class Emotion(Enum):
    """Simple emotion categories influencing tension."""
    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"

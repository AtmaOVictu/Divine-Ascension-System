from enum import Enum

class Emotion(Enum):
    """Enumeration of possible emotional states with default intensities."""
    NEUTRAL = 0.0
    FEAR = 0.6
    JOY = 0.4
    ANGER = 0.8
    SORROW = 0.5

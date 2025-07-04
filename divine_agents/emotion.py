from enum import Enum

class EmotionType(Enum):
    """Basic emotion types influencing an agent's responses."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"

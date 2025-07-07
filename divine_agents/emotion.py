from enum import Enum, auto


class Emotion(Enum):
    """Enumeration of basic emotions that influence agent responses."""

    NEUTRAL = auto()
    FEAR = auto()
    JOY = auto()
    ANGER = auto()
    SORROW = auto()

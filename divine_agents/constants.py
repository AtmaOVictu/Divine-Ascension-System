"""Constants governing agent behavior."""

EMOTION_THRESHOLD = 0.5
TENSION_THRESHOLD = 0.7
MAX_EMOTION = 1.0
MIN_EMOTION = 0.0

def is_emotion_high(value: float) -> bool:
    """Return True if emotion intensity exceeds the threshold."""
    return value >= EMOTION_THRESHOLD

def is_tension_high(value: float) -> bool:
    """Return True if tension exceeds the threshold."""
    return value >= TENSION_THRESHOLD

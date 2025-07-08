import math

EMOTION_DECAY = {
    "calm": 0.1,
    "neutral": 0.3,
    "anger": 0.4,
    "joy": 0.05,
}


def calculate_tension_decay(emotion: str, tension: float, time_step: float) -> float:
    """Return decayed tension based on emotional state."""
    rate = EMOTION_DECAY.get(emotion, EMOTION_DECAY["neutral"])
    return tension * math.exp(-rate * time_step)

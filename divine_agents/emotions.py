"""Emotion utilities for agent tension and dialogue prefixes."""

EMOTION_TENSION_FACTOR = {
    'fear': 1.0,
    'joy': 0.5,
    'anger': 0.8,
    'sorrow': 0.7,
    'neutral': 0.0,
}

EMOTION_PREFIX = {
    'fear': 'V strahu',
    'joy': 'Z veseljem',
    'anger': 'Z jezo',
    'sorrow': 'S žalostjo',
    'neutral': '',
}

def tension_from_emotion(emotion: str, intensity: float) -> float:
    """Return additional tension caused by the given emotion intensity."""
    factor = EMOTION_TENSION_FACTOR.get(emotion, 0.5)
    return intensity * factor

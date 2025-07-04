# Emotion intensity mapping used for agent tension adjustments.
EMOTION_INTENSITY = {
    "fear": 0.6,
    "joy": 0.4,
    "anger": 0.7,
    "sorrow": 0.5,
}


def get_intensity(emotion: str) -> float:
    """Return the numeric intensity for the given emotion name."""
    return EMOTION_INTENSITY.get(emotion.lower(), 0.0)

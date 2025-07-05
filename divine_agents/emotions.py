EMOTION_INTENSITY = {
    'fear': 0.6,
    'joy': 0.4,
    'anger': 0.7,
}

def emotion_to_intensity(name: str) -> float:
    """Return intensity for a given emotion name."""
    return EMOTION_INTENSITY.get(name, 0.0)

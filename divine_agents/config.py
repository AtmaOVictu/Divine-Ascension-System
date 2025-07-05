import os


def get_tension_threshold() -> float:
    """Return tension threshold from environment or default to 0.7."""
    return float(os.getenv("TENSION_THRESHOLD", 0.7))


def get_emotion_threshold() -> float:
    """Return emotion threshold from environment or default to 0.5."""
    return float(os.getenv("EMOTION_THRESHOLD", 0.5))

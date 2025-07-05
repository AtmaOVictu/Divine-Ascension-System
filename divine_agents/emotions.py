"""Utility structures for handling basic emotions."""

from enum import Enum


class Emotion(Enum):
    FEAR = "strah"
    JOY = "veselje"
    ANGER = "jeza"
    SORROW = "potrtost"
    NEUTRAL = "brezcutno"


def is_negative(emotion: Emotion) -> bool:
    """Return True if emotion is generally negative."""
    return emotion in {Emotion.FEAR, Emotion.ANGER, Emotion.SORROW}

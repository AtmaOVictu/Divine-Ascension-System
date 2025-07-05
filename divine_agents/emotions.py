# -*- coding: utf-8 -*-
"""Collection of emotions mapped to intensity values.

This module defines a basic mapping of common emotions to a numerical
scale used by the ontological agents. The values range from -1 for
strongly negative emotions to 1 for strongly positive emotions. A value
of 0 denotes a neutral state.
"""

EMOTION_SCALE = {
    "sreca": 1,
    "zalost": -1,
    "strah": -1,
    "jeza": -1,
    "presenecenje": 0,
    "zadovoljstvo": 1,
    "ljubezen": 1,
    "krivda": -1,
    "upanje": 1,
    "osamljenost": -1,
    "skrb": -1,
    "hvaleznost": 1,
    "sram": -1,
    "mir": 1,
}


def get_intensity(emotion_name: str) -> float:
    """Return the intensity value for a given emotion name."""
    return EMOTION_SCALE.get(emotion_name.lower(), 0.0)

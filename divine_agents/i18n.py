# -*- coding: utf-8 -*-
"""Internationalization helpers for agent responses."""

# Supported languages
LANGUAGES = ("sl", "en")

# Mapping of ontological state to translations
RESPONSES = {
    "Ego": {
        "sl": "Resnica je absolutna in neodvisna od drugih.",
        "en": "Truth is absolute and independent of others.",
    },
    "Jaz": {
        "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
        "en": "Truth is relative, shaped by our relationships.",
    },
    "Enotnost": {
        "sl": "Vse resnice so eno, medsebojno povezane.",
        "en": "All truths are one, interconnected.",
    },
}

# Simple translation for the main question used in dialogues
QUESTION = {
    "sl": "Kaj je resnica?",
    "en": "What is truth?",
}

"""Ontological dictionary mapping words to emotional context."""
from typing import Dict


class OntologicalDictionary:
    """Dictionary containing emotional and philosophical meanings of words."""

    def __init__(self) -> None:
        self._data: Dict[str, Dict[str, object]] = {
            "fear": {
                "emotion": "negative",
                "philosophical_meaning": "response to the unknown",
                "emotional_intensity": 0.9,
            },
            "joy": {
                "emotion": "positive",
                "philosophical_meaning": "harmony with self",
                "emotional_intensity": 0.7,
            },
            "anger": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived injustice",
                "emotional_intensity": 0.8,
            },
        }

    def get_word_meaning(self, word: str) -> Dict[str, object]:
        """Return meaning information about a word."""
        return self._data.get(
            word,
            {
                "emotion": "unknown",
                "philosophical_meaning": "unknown",
                "emotional_intensity": 0.0,
            },
        )

    def update_word_meaning(self, word: str, meaning: Dict[str, object]) -> None:
        """Update or add new word meaning."""
        self._data[word] = meaning

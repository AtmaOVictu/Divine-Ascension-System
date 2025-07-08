"""Ontological dictionary module for emotional and philosophical meanings."""

from typing import Dict, Any


class OntologicalDictionary:
    """Map words to emotional and philosophical contexts."""

    def __init__(self) -> None:
        # Basic mapping of words to their meanings and intensities
        self.dictionary: Dict[str, Dict[str, Any]] = {
            "fear": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to danger",
                "emotional_intensity": 0.8,
            },
            "joy": {
                "emotion": "positive",
                "philosophical_meaning": "harmony with existence",
                "emotional_intensity": 0.4,
            },
            "anger": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived injustice",
                "emotional_intensity": 0.9,
            },
            "calm": {
                "emotion": "positive",
                "philosophical_meaning": "equilibrium of mind",
                "emotional_intensity": 0.2,
            },
        }

    def get_word_meaning(self, word: str) -> Dict[str, Any]:
        """Retrieve meaning of a word with emotional context."""
        return self.dictionary.get(
            word,
            {"emotion": "unknown", "philosophical_meaning": "unknown", "emotional_intensity": 0.0},
        )

    def update_word_meaning(self, word: str, meaning: Dict[str, Any]) -> None:
        """Update or insert a word's meaning."""
        self.dictionary[word] = meaning

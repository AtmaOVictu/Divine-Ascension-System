class OntologicalDictionary:
    """Dictionary mapping words to emotional and philosophical meaning."""

    def __init__(self) -> None:
        self.dictionary = {
            "anger": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived injustice",
                "emotional_intensity": 8,
            },
            "calm": {
                "emotion": "positive",
                "philosophical_meaning": "equilibrium of mind",
                "emotional_intensity": 2,
            },
            "truth": {
                "emotion": "neutral",
                "philosophical_meaning": "the essence of reality",
                "emotional_intensity": 5,
            },
        }

    def get_word_meaning(self, word: str) -> dict:
        """Return emotional and philosophical context for a word."""
        return self.dictionary.get(
            word,
            {"emotion": "unknown", "philosophical_meaning": "unknown", "emotional_intensity": 0},
        )

    def update_word_meaning(self, word: str, meaning: dict) -> None:
        """Update or add a word's meaning."""
        self.dictionary[word] = meaning

class OntologicalDictionary:
    """Map words to emotional and philosophical context."""

    def __init__(self):
        self.dictionary = {
            "anger": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived injustice",
                "emotional_intensity": 0.8,
            },
            "calm": {
                "emotion": "positive",
                "philosophical_meaning": "equilibrium of mind",
                "emotional_intensity": 0.2,
            },
            "truth": {
                "emotion": "neutral",
                "philosophical_meaning": "the essence of reality",
                "emotional_intensity": 0.5,
            },
        }

    def get_word_meaning(self, word: str) -> dict:
        """Return meaning for the given word."""
        return self.dictionary.get(
            word,
            {
                "emotion": "unknown",
                "philosophical_meaning": "unknown",
                "emotional_intensity": 0.0,
            },
        )

    def update_word_meaning(self, word: str, meaning: dict) -> None:
        """Update dictionary with a new meaning."""
        self.dictionary[word] = meaning

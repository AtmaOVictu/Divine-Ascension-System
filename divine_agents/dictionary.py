class OntologicalDictionary:
    """Map words to emotional and philosophical meanings."""

    def __init__(self):
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
        """Retrieve the meaning for a given word."""
        return self.dictionary.get(
            word,
            {
                "emotion": "unknown",
                "philosophical_meaning": "unknown",
                "emotional_intensity": 0,
            },
        )

    def update_word_meaning(self, word: str, meaning: dict) -> None:
        """Update the meaning of a word."""
        self.dictionary[word] = meaning

class OntologicalDictionary:
    """Dictionary mapping words to emotional and philosophical meaning."""

    def __init__(self):
        self.dictionary = {
            "fear": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived danger",
                "intensity": 0.8,
            },
            "joy": {
                "emotion": "positive",
                "philosophical_meaning": "state of happiness",
                "intensity": 0.6,
            },
            "anger": {
                "emotion": "negative",
                "philosophical_meaning": "reaction to perceived injustice",
                "intensity": 0.7,
            },
        }

    def get_word_meaning(self, word: str) -> dict:
        """Return emotional and philosophical meaning for a word."""
        return self.dictionary.get(word, {
            "emotion": "neutral",
            "philosophical_meaning": "unknown",
            "intensity": 0.0,
        })

    def update_word_meaning(self, word: str, meaning: dict) -> None:
        """Update the dictionary with a new meaning."""
        self.dictionary[word] = meaning

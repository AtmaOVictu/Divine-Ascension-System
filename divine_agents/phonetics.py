class PhoneticTruthMap:
    """Map phonetic inputs to philosophical meanings."""

    def __init__(self) -> None:
        self.phonetic_truths = {
            "ba": "truth",
            "ka": "negation",
            "da": "being",
            "ma": "nothing",
            "ra": "wisdom",
            "š": "spiritual seeking",
            "č": "transformation",
            "ž": "growth",
            "ć": "transition",
            "đ": "in-between",
            "ja": "affirmation",
        }

    def map_phonetic_input(self, phoneme: str) -> str:
        """Return mapped meaning for a given phoneme."""
        return self.phonetic_truths.get(phoneme, "undefined")

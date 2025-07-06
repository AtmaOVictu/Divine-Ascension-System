class PhoneticTruthMap:
    """Map phonetic inputs to ontological meanings."""

    def __init__(self) -> None:
        self.phonetic_truths = {
            "ba": "truth",        # Absolutna resnica
            "ka": "negation",     # Negacija
            "da": "being",        # Bivanje
            "ma": "nothing",      # Nič
            "ra": "wisdom",       # Modrost
            "š": "spiritual seeking",  # Iskanje duhovnega
            "č": "transformation",     # Transformacija
            "ž": "growth",             # Rast
            "ć": "transition",         # Prehod
            "đ": "in-between",         # Vmesno stanje
            "ja": "affirmation",       # Potrditev
        }

    def map_phonetic_input(self, phoneme: str) -> str:
        """Return ontological meaning for the given phoneme."""
        return self.phonetic_truths.get(phoneme, "undefined")

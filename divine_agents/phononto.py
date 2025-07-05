"""Phoneme based ontological transitions."""

class FonontoTransition:
    """Map phoneme transitions to ontological meaning."""

    def __init__(self, phoneme_start: str, phoneme_end: str):
        self.phoneme_start = phoneme_start
        self.phoneme_end = phoneme_end
        self.ontological_meaning = None

    def apply_transition(self) -> str:
        """Return ontological meaning for the transition."""
        self.ontological_meaning = self.get_ontological_meaning()
        return self.ontological_meaning

    def get_ontological_meaning(self) -> str:
        meanings = {
            "O": "Potencialnost, začetek",
            "N": "Dejanje, prehod",
            "T": "Transformacija",
            "Z": "Nič, praznina",
            "A": "Akcija, dejanje",
        }
        return meanings.get(self.phoneme_end, "Neznan prehod")

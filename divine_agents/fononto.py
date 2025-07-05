"""Fononto-related classes for phonetic-ontological transitions."""

from typing import Dict


class FonontoTransition:
    """Represents a phoneme transition with ontological meaning."""

    meanings: Dict[str, str] = {
        "O": "Potencialnost, začetek",
        "N": "Dejanje, prehod",
        "T": "Transformacija",
        "Z": "Nič, praznina",
        "A": "Akcija, dejanje",
    }

    def __init__(self, phoneme_start: str, phoneme_end: str) -> None:
        self.phoneme_start = phoneme_start
        self.phoneme_end = phoneme_end
        self.ontological_meaning = None

    def apply_transition(self) -> str:
        """Return ontological meaning of the phoneme transition."""
        self.ontological_meaning = self.meanings.get(
            self.phoneme_end, "Neznan prehod"
        )
        return self.ontological_meaning


class OntologicalPhase:
    """Sequence of phoneme transitions representing an ontological phase."""

    def __init__(self, name: str, phoneme_start: str, phoneme_end: str) -> None:
        self.name = name
        self.transition = FonontoTransition(phoneme_start, phoneme_end)

    def begin_phase(self) -> str:
        """Begin the phase and return its ontological meaning."""
        return self.transition.apply_transition()

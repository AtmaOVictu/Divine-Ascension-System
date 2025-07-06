"""Resonance and phonetic mapping utilities."""
from typing import List


class ResonanceAgent:
    """Agent that evolves its resonance based on phonetic truths."""

    def __init__(self, initial_resonance: float = 0.5) -> None:
        self.resonance_level = initial_resonance

    def evolve_resonance(self, phonetic_truths: List[str]) -> float:
        """Update resonance level based on a list of truth labels."""
        for truth in phonetic_truths:
            if truth == "truth":
                self.resonance_level += 0.1
            elif truth == "negation":
                self.resonance_level -= 0.1
            elif truth == "wisdom":
                self.resonance_level += 0.2

        # keep value within [0, 1]
        self.resonance_level = max(0.0, min(1.0, self.resonance_level))
        return self.resonance_level


class PhoneticTruthMap:
    """Map phonemes to their philosophical meanings."""

    def __init__(self) -> None:
        self.phonetic_truths = {
            "ba": "truth",
            "ka": "negation",
            "da": "being",
            "ma": "nothing",
            "ra": "wisdom",
        }

    def map_phonetic_input(self, phoneme: str) -> str:
        """Return the truth label for a given phoneme."""
        return self.phonetic_truths.get(phoneme, "undefined")

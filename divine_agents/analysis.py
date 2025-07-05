from typing import List

class SymbolicAI:
    """Simplified symbolic reasoning engine for dialogue analysis."""

    def analyze(self, text: str) -> str:
        """Classify a line of dialogue based on truth semantics."""
        lowered = text.lower()
        if "absolut" in lowered:
            return "Ego"
        if "relativ" in lowered:
            return "Jaz"
        if "eno" in lowered:
            return "Enotnost"
        return "Neznano"


def analyze_dialogue(lines: List[str]) -> List[str]:
    """Analyze a series of dialogue lines and return the inferred states."""
    ai = SymbolicAI()
    return [ai.analyze(line) for line in lines]


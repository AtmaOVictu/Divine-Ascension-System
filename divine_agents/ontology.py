from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Concept:
    """Represents a word with its connotations and category."""
    name: str
    category: str
    connotations: List[str]


_CONCEPTS: Dict[str, Concept] = {
    "ljubezen": Concept("ljubezen", "čustvo", ["toplina", "zaupanje"]),
    "svoboda": Concept("svoboda", "filozofski koncept", ["optimizem", "izbira"]),
    "strah": Concept("strah", "čustvo", ["negotovost", "napetost"]),
}


def categorize(word: str) -> Optional[Concept]:
    """Return the Concept associated with a word if known."""
    return _CONCEPTS.get(word.lower())

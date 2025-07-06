import random
from typing import Tuple, Optional


class OntologicalOppositesGenerator:
    """Generate ontological opposites and transitions between them."""

    def __init__(self) -> None:
        # Basic opposites mapping
        self.opposites = {
            "biti": "ničnost",
            "tišina": "zven",
            "ego": "jaz",
            "resnica": "laž",
            "svetloba": "tema",
            "umirjenost": "jeza",
            "vednost": "nevednost",
        }

    def generate_opposites(self) -> Tuple[str, str]:
        """Randomly return a pair of opposites."""
        return random.choice(list(self.opposites.items()))

    def create_transition(self, state: str) -> str:
        """Return a text describing the transition from state to its opposite."""
        opposite: Optional[str] = self.opposites.get(state)
        if opposite:
            return f"Prehod iz {state} v {opposite}."
        return f"Nema nasprotja za {state}."

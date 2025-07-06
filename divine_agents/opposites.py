import random
from typing import Tuple

class OntologicalOppositesGenerator:
    """Generate pairs of ontological opposites and build transitions."""

    def __init__(self) -> None:
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
        """Return a randomly selected pair of opposites."""
        return random.choice(list(self.opposites.items()))

    def create_transition(self, state: str) -> str:
        """Return a textual description of a transition to the opposite state."""
        opposite = self.opposites.get(state)
        if opposite:
            return f"Prehod iz {state} v {opposite}."
        return f"Nema nasprotja za {state}."

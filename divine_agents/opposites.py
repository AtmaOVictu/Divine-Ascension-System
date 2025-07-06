import random

class OntologicalOppositesGenerator:
    """Generate ontological opposites and provide transitions."""

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

    def generate_opposites(self) -> tuple[str, str]:
        """Return a random pair of opposites."""
        return random.choice(list(self.opposites.items()))

    def get_opposite(self, state: str) -> str | None:
        """Return the opposite of the given state if available."""
        return self.opposites.get(state)

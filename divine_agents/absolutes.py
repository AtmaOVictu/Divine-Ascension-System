import random


class RelativeAbsoluteLibrary:
    """A conceptual library where absolutes are influenced by context."""

    def __init__(self) -> None:
        self.constants = {
            "truth": 1.0,
            "time": 1.0,
        }

    def get_absolute(self, concept: str) -> float:
        """Return an absolute value modified by a relative factor."""
        base = self.constants.get(concept)
        if base is None:
            raise ValueError(f"Unknown concept: {concept}")
        return base * self.relative_factor(concept)

    def relative_factor(self, concept: str) -> float:
        """Compute a factor that changes with context."""
        if concept == "truth":
            return random.uniform(0.5, 1.5)
        if concept == "time":
            return random.uniform(0.8, 1.2)
        return 1.0

    def set_absolute(self, concept: str, value: float) -> None:
        """Set the base absolute value for a concept."""
        self.constants[concept] = value

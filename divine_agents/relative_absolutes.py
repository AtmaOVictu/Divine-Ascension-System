import random

class RelativeAbsoluteLibrary:
    """Library representing mutable absolute concepts."""

    def __init__(self):
        self.constants = {"truth": 1.0, "time": 1.0}

    def relative_factor(self, concept: str) -> float:
        """Return a contextual factor altering an absolute concept."""
        if concept == "truth":
            return random.uniform(0.5, 1.5)
        if concept == "time":
            return random.uniform(0.8, 1.2)
        return 1.0

    def get_absolute(self, concept: str) -> float | None:
        """Retrieve the current absolute value of a concept."""
        if concept not in self.constants:
            return None
        return self.constants[concept] * self.relative_factor(concept)

    def set_absolute(self, concept: str, value: float) -> None:
        """Define a new absolute value for a concept."""
        self.constants[concept] = value

import random


class RelativeAbsoluteLibrary:
    """Library providing mutable absolute concepts."""

    def __init__(self) -> None:
        self.constants = {"truth": 1.0, "time": 1.0}

    def get_absolute(self, concept: str) -> float:
        base = self.constants.get(concept, 0)
        return base * self.relative_factor(concept)

    def relative_factor(self, concept: str) -> float:
        if concept == "truth":
            return random.uniform(0.5, 1.5)
        if concept == "time":
            return random.uniform(0.8, 1.2)
        return 1.0

    def set_absolute(self, concept: str, value: float) -> None:
        self.constants[concept] = value

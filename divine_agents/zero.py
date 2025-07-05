"""Module providing a zero or neutral space for stabilization."""


class Niclo:
    """Represents a zero space where an agent can stabilize."""

    def __init__(self) -> None:
        self.state = "mirno"

    def stabilizacija(self) -> str:
        """Stabilize and return the new state."""
        self.state = "stabilno"
        return self.state

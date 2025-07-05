class SecondTrueAxis:
    """Determines orientation based on oscillation between light and dark."""

    def __init__(self, name: str, oscillation: float):
        self.name = name
        self.oscillation = oscillation
        self.direction = "neutral"

    def determine_direction(self) -> str:
        """Return direction based on oscillation."""
        self.direction = "proactive" if self.oscillation > 0.5 else "defensive"
        return self.direction

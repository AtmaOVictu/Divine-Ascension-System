class NullSpace:
    """Represents a calm state waiting for activation."""

    def __init__(self):
        self.state = "calm"

    def stabilize(self) -> None:
        """Bring the system into a stable zero state."""
        self.state = "stable"

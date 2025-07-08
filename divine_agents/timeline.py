class Timeline:
    """Track discrete time steps for agents."""

    def __init__(self) -> None:
        self.tick_count = 0

    def tick(self) -> int:
        """Advance the timeline and return the current step."""
        self.tick_count += 1
        return self.tick_count

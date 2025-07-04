class OuroborosCycle:
    """Maintain an endless cycle through ontological states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, start_state: str = "Ego") -> None:
        if start_state not in self.STATES:
            raise ValueError(f"Unknown state: {start_state}")
        self.state = start_state
        self.history = [start_state]

    def cycle(self) -> str:
        """Advance to the next state in the ouroboros cycle."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        else:
            self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def get_history(self):
        return self.history

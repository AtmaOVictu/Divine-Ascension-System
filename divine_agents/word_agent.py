"""Module containing the WordAgent class for dynamic word transitions."""

class WordAgent:
    """Represents a word as an active agent within the system."""

    def __init__(self, word: str):
        self.word = word
        self.state = "inactive"
        self.energy = 0.0

    def activate(self) -> None:
        """Activate the word agent by increasing energy and setting state."""
        self.state = "active"
        self.energy = 0.5

    def transition(self) -> str:
        """Transition the word through different energetic states."""
        if self.state == "active":
            self.state = "energized"
            self.energy = 1.0
        elif self.state == "energized":
            self.state = "resonating"
        return self.state

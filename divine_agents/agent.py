class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        emotions: dict | None = None,
        tension: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.emotions = emotions or {"anger": 0.0, "joy": 0.0, "fear": 0.0}
        self.tension = tension
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update the value of a specific emotion and recalculate tension."""
        self.emotions[emotion_type] = value
        self.calculate_tension()

    def calculate_tension(self) -> None:
        """Calculate tension as the average of all emotion values."""
        self.tension = sum(self.emotions.values()) / len(self.emotions)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotions.values()):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def interact(self, other: "Agent") -> None:
        """Simple interaction affecting emotions based on different states."""
        if self.state != other.state:
            self.update_emotion("anger", self.emotions.get("anger", 0.0) + 0.1)
            other.update_emotion("fear", other.emotions.get("fear", 0.0) + 0.1)

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        self.emotions[name] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_trigger = any(v > 0.5 for v in self.emotions.values())
        if self.tension > 0.7 or emotion_trigger:
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

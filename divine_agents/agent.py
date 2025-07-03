class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {"joy": 0.0, "fear": 0.0, "anger": 0.0}
        if emotions:
            for key, value in emotions.items():
                if key in self.emotions:
                    self.emotions[key] = value
        self.history = [state]

    @property
    def aggregated_emotion(self) -> float:
        """Return the summed intensity of all tracked emotions."""
        return sum(self.emotions.values())

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update specific emotion intensity and adjust tension accordingly."""
        if emotion_type not in self.emotions:
            raise ValueError(f"Unknown emotion '{emotion_type}'")
        self.emotions[emotion_type] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.aggregated_emotion > 0.5:
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

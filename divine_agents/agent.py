class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def _recalculate_tension(self) -> None:
        """Update tension based on current emotions."""
        self.tension = max(self.emotions.values())

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update a specific emotion and adjust tension."""
        if emotion_type in self.emotions:
            self.emotions[emotion_type] = value
            self._recalculate_tension()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_high = any(v > 0.5 for v in self.emotions.values())
        if self.tension > 0.7 or emotion_high:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        dominant = max(self.emotions, key=self.emotions.get)
        prefix_map = {"fear": "Zaskrbljeno, ", "joy": "Veselo, ", "anger": "Jezno, "}
        prefix = prefix_map[dominant] if self.emotions[dominant] > 0 else ""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}"

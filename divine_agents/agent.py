class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension: float = 0.0
        # emotions are stored as a mapping of emotion name to intensity [0, 1]
        self.emotions: dict[str, float] = {}
        self.history = [state]

    def express_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion intensity and increase tension."""
        self.emotions[name] = intensity
        self.tension += intensity

    # Backwards compatibility for simple emotion update
    def update_emotion(self, value: float) -> None:  # pragma: no cover - kept for API compatibility
        self.express_emotion("general", value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _current_emotion_intensity(self) -> float:
        return max(self.emotions.values()) if self.emotions else 0.0

    def dominant_emotion(self) -> str | None:
        """Return the emotion with the highest intensity."""
        if not self.emotions:
            return None
        return max(self.emotions, key=self.emotions.get)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._current_emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        statement = base.get(self.state, "")
        emotion = self.dominant_emotion()
        feeling = f" Občutim {emotion}." if emotion else ""
        return statement + feeling

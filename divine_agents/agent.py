class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion & tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = min(1.0, value)

    # ------------------------------------------------------------------
    # State logic
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"Čutim {self.emotion_type}. " if self.emotion > 0.5 else ""
        return prefix + self.PHILOSOPHY[self.state]

class Agent:
    """Ontological agent that can transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set an emotion and update internal tension."""
        self.emotion_label = label
        self.update_emotion(intensity)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label:
            response += f" Občutim {self.emotion_label}."
        return response

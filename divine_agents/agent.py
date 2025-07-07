"""Ontological agents capable of emotional state transitions and dialogue."""

class Agent:
    """Represents an ontological agent with emotion driven state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Base philosophical responses for each ontological state.
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

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
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # emotion influences tension build-up
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
        base = self.PHILOSOPHY.get(self.state, "")
        emotion_note = {
            "fear": " Občutim strah.",
            "joy": " Napolnjuje me veselje.",
            "anger": " Občutim jezo.",
            "sorrow": " Preveva me žalost.",
        }.get(self.emotion_label, "")
        return base + emotion_note

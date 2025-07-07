class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_value: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_value = emotion_value
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, kind: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on the emotion."""
        self.emotion_type = kind
        self.emotion_value = value
        if kind in ("fear", "anger"):
            self.tension += value
        elif kind == "joy":
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_value > 0.5:
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
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }[self.state]

        prefix = {
            "fear": "S tresočim glasom",
            "anger": "Z jezo",
            "joy": "Z veseljem",
        }.get(self.emotion_type, "Mirno")

        return f"{prefix} povem: {base}"

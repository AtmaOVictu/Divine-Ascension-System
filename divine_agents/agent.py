class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def apply_emotion(self, emotion_type: str, intensity: float) -> None:
        """Apply an emotion and modify tension based on its type."""
        self.emotion_type = emotion_type
        self.update_emotion(intensity)
        if emotion_type in {"fear", "anger"}:
            self.tension += 0.2
        elif emotion_type == "joy":
            self.tension = max(self.tension - 0.1, 0.0)

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = {
            "fear": "s strahom",
            "anger": "z jezo",
            "joy": "z veseljem",
        }.get(self.emotion_type, "")

        return f"{mood} {base}".strip()

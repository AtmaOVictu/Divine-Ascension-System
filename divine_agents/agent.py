class Agent:
    """Represent an ontological agent that can shift philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: str = "neutral", emotion_intensity: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_intensity = emotion_intensity
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Set emotion and increase tension based on intensity."""
        self.emotion = emotion
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition agent state when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_prefix(self) -> str:
        """Return a phrase that reflects the agent's current emotion."""
        mapping = {
            "fear": "V strahu povem, da",
            "anger": "Z jezo trdim, da",
            "joy": "Z veseljem pravim, da",
        }
        return mapping.get(self.emotion, "Menim, da")

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{self._emotion_prefix()} {base}"

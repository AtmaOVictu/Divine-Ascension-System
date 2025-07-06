class Agent:
    """Ontological agent capable of state transitions driven by emotions and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    # Mapping of emotion names to intensity values used for tension updates.
    EMOTION_VALUES = {
        "neutral": 0.0,
        "fear": 0.6,
        "joy": 0.4,
        "anger": 0.7,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_name = emotion
        self.emotion = self._emotion_intensity(emotion)
        self.history = [state]

    def _emotion_intensity(self, emotion) -> float:
        """Return numerical intensity for a given emotion."""
        if isinstance(emotion, str):
            return float(self.EMOTION_VALUES.get(emotion, 0.0))
        return float(emotion)

    def update_emotion(self, emotion) -> None:
        """Update emotion type or intensity and adjust tension accordingly."""
        intensity = self._emotion_intensity(emotion)
        if isinstance(emotion, str):
            self.emotion_name = emotion
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer based on current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        return f"{base} (Čustvo: {self.emotion_name})"

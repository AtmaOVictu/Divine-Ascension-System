class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Influence of a given emotion on tension.
    EMOTION_INFLUENCE = {
        "fear": 0.3,
        "anger": 0.4,
        "joy": 0.1,
        "sorrow": 0.2,
        "neutral": 0.0,
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update unnamed emotion intensity and adjust tension."""
        self.set_emotion("neutral", value)

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion with name and update tension accordingly."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity * self.EMOTION_INFLUENCE.get(name, 0.0)

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
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        return f"{base} Čutim {self.emotion_name}."

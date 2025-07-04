class Agent:
    """Ontological agent capable of transitioning states based on emotions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_EFFECT = {
        "fear": 0.3,
        "anger": 0.5,
        "joy": -0.2,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion and adjust tension based on its type."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity
        self.tension += self.EMOTION_EFFECT.get(emotion_type, 0.0)
        if self.tension < 0:
            self.tension = 0.0

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
        """Return a philosophical answer influenced by current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (občutek: {self.emotion_type})"

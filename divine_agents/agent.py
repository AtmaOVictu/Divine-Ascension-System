class Agent:
    """Represent an ontological agent capable of state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion_type = emotion_type
        self.emotion = value
        if emotion_type in ("fear", "anger"):
            self.tension += value
        elif emotion_type == "joy":
            self.tension -= value * 0.5
        else:
            self.tension += value * 0.2
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_prefix = {
            "fear": "S strahom povem, da ",
            "anger": "Z jezo trdim, da ",
            "joy": "V radosti menim, da ",
        }.get(self.emotion_type, "")

        return f"{emotion_prefix}{base}"

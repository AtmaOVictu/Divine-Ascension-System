class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger", "neutral")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if emotion_type not in self.EMOTIONS:
            emotion_type = "neutral"
        self.emotion_type = emotion_type
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
        prefix = {
            "fear": "S strahom ",
            "joy": "Z veseljem ",
            "anger": "Z jezo ",
            "neutral": "",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            return f"{prefix}verjamem, da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}verjamem, da je resnica relativna, oblikovana z našimi odnosi."
        return f"{prefix}verjamem, da so vse resnice eno, medsebojno povezane."

class Agent:
    """Represent an ontological agent with emotions and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", *,
                 tension: float = 0.0, emotion_level: float = 0.0,
                 emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_level = value
        self.tension += value

    def set_emotion_type(self, emotion: str) -> None:
        """Set the descriptive emotion type (fear, joy, anger, etc.)."""
        if emotion in self.EMOTIONS:
            self.emotion_type = emotion
        else:
            self.emotion_type = "neutral"

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
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

        if self.emotion_type == "fear":
            prefix = "(Strah)"
        elif self.emotion_type == "joy":
            prefix = "(Veselje)"
        elif self.emotion_type == "anger":
            prefix = "(Jeza)"
        else:
            prefix = ""

        return f"{prefix} {base}".strip()

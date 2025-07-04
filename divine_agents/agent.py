class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_LEVELS = {
        "joy": 0.8,
        "fear": 0.6,
        "anger": 0.7,
        "sorrow": 0.4,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, emotion_type: str) -> None:
        """Set emotion using predefined emotion types."""
        if emotion_type not in self.EMOTION_LEVELS:
            raise ValueError(f"Unknown emotion type: {emotion_type}")
        self.update_emotion(self.EMOTION_LEVELS[emotion_type])

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
        prefix = ""
        if self.emotion > 0.7:
            prefix = "Strastno menim, da "
        elif self.emotion > 0.4:
            prefix = "Menim, da "
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base

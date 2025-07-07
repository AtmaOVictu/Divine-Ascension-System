class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_EFFECTS = {
        "fear": 0.6,
        "anger": 0.7,
        "joy": 0.4,
        "sorrow": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, emotion_label: str) -> None:
        """Apply a named emotion and update tension accordingly."""
        self.emotion_label = emotion_label
        effect = self.EMOTION_EFFECTS.get(emotion_label, 0.1)
        self.update_emotion(effect)

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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label != "neutral":
            return f"Občutim {self.emotion_label}, zato menim: {base}"
        return base

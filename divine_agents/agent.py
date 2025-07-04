from .principles import EGO_PRINCIPLE, JAZ_PRINCIPLE, ENOTNOST_PRINCIPLE


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if label is not None:
            self.emotion_label = label

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
        if self.state == "Ego":
            base = EGO_PRINCIPLE
        elif self.state == "Jaz":
            base = JAZ_PRINCIPLE
        else:
            base = ENOTNOST_PRINCIPLE

        if self.emotion_label == "anger":
            return base.upper()
        if self.emotion_label == "joy":
            return f":) {base}"
        if self.emotion_label == "fear":
            return f"...{base}"
        return base

class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *,
                 tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "nevtralnost"
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity and adjust tension."""
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
        """Return a philosophical answer reflecting state and emotion."""
        emotional_phrase = f"ob \"{self.emotion_type}\"" if self.emotion_type else ""
        if self.state == "Ego":
            return (
                f"{emotional_phrase} verjamem, da je resnica absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"{emotional_phrase} razumem resnico kot relativno, oblikovano z našimi odnosi."
            )
        return (
            f"{emotional_phrase} zaznavam, da so vse resnice eno, medsebojno povezane."
        )

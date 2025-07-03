class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    # Default thresholds controlling when a transition should occur
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        tension_threshold: float | None = None,
        emotion_threshold: float | None = None,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Allow custom thresholds per instance while defaulting to class values
        self.tension_threshold = (
            tension_threshold if tension_threshold is not None else self.TENSION_THRESHOLD
        )
        self.emotion_threshold = (
            emotion_threshold if emotion_threshold is not None else self.EMOTION_THRESHOLD
        )

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.tension_threshold or self.emotion > self.emotion_threshold:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str = "neutral"):
        """Initialize the agent with its state and emotional context."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity.
        name:
            Optional name describing the emotion (e.g. 'fear', 'joy').
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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
        emotion_info = f" (emotion: {self.emotion_name} {self.emotion:.2f})"
        if self.state == "Ego":
            return "Truth is absolute and independent of others." + emotion_info
        if self.state == "Jaz":
            return "Truth is relative, shaped by our relationships." + emotion_info
        return "All truths are one, interconnected." + emotion_info

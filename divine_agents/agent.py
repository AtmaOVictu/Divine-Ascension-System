class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        """Initialize the agent with state, tension and emotion settings."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            Intensity of the emotion in the ``0-1`` range.
        emotion_type:
            Optional name of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type

        # Negative emotions cause a larger tension increase
        if self.emotion_type in {"fear", "anger"}:
            self.tension += value
        else:
            self.tension += value * 0.5

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_prefix = {
            "fear": "V strahu",
            "joy": "V radosti",
            "anger": "V jezi",
            "sorrow": "V žalosti",
        }.get(self.emotion_type, "")

        return f"{emotion_prefix} {base}".strip()

"""Core classes for the Divine Ascension agent framework."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Display name for the agent.
        state:
            Initial ontological state.
        tension:
            Current tension level.
        emotion:
            Current emotion intensity (0-1 scale).
        emotion_type:
            Name of the emotion affecting the agent (e.g. ``"fear"``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        # The stronger the emotion, the greater the tension.
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
        """Return a philosophical answer depending on the current state.

        Emotional context slightly colours the response text.
        """
        prefix = f"Ob čustvu '{self.emotion_type}', """
        if self.state == "Ego":
            return prefix + "resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "vse resnice so eno, medsebojno povezane."

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *,
                 tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str = "neutral") -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent's identifier.
        state:
            Initial ontological state.
        tension:
            Current level of tension influencing state transitions.
        emotion:
            Intensity of the agent's emotion.
        emotion_type:
            Descriptor of the current emotion (e.g. ``fear`` or ``joy``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its type.

        Parameters
        ----------
        value:
            New intensity of the emotion.
        emotion_type:
            If provided, set the current emotion descriptor.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # Emotion intensity contributes to the overall tension
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

        The response also reflects the agent's current emotion.
        """
        prefix = f"(občuti {self.emotion_type}) " if self.emotion_type != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

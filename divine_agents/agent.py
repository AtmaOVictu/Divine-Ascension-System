class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, thresholds: list = None):
        """Create a new agent with optional custom thresholds.

        Parameters
        ----------
        name: str
            Identifier for the agent.
        state: str
            Initial ontological state. Defaults to "Ego".
        tension: float
            Initial tension level.
        emotion: float
            Initial emotion intensity.
        thresholds: list, optional
            Ordered list of threshold values between 0 and 1 that trigger
            state transitions. If not provided, defaults to ``[0.1, ..., 1.0]``.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.thresholds = thresholds or [i / 10 for i in range(1, 11)]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if any threshold is exceeded."""
        for threshold in self.thresholds:
            if self.tension >= threshold or self.emotion >= threshold:
                if self.state == "Ego":
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    self.state = "Enotnost"
                break
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

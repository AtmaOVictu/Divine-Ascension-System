class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion by ``value`` and mirror it to tension.

        The emotional intensity is accumulated and the resulting value is also
        used as the current tension level.  This tight coupling reflects how
        strong feelings directly manifest as internal tension which can trigger
        state transitions.
        """
        self.emotion += value
        self.tension = self.emotion

    def update_tension(self, value: float) -> None:
        """Set the agent's tension to ``value``.

        This method allows external events to directly influence the agent's
        tension without altering its emotional state.
        """
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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

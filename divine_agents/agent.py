class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        If the provided emotion does not exceed the transition threshold
        (0.5), it is nudged by ``0.01`` to ensure potential progression.
        """
        self.emotion = value
        if self.emotion <= 0.5:
            self.emotion += 0.01
        self.tension += self.emotion

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

        The response intensity reflects the agent's current emotional level.
        """
        if self.state == "Ego":
            statement = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{statement} (občuti intenziteto {self.emotion:.2f})"
        return statement

class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level in the range ``0``-``1``.
    emotion:
        Current emotional intensity in the range ``0``-``1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity in the range ``0``-``1``. Values are clamped
            to this range. The tension is increased by the same value.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level within ``0``-``1`` bounds."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform state transition if tension or emotion thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The response is lightly coloured by the current emotional intensity.
        """
        mood = ""
        if self.emotion > 0.5:
            mood = " z veliko strastjo"
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + mood

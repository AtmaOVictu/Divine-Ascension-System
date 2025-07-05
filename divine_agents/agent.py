class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique identifier of the agent.
    state:
        One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Current level of inner tension in the range ``0.0`` - ``1.0``.
    emotion:
        Current emotional intensity in the range ``0.0`` - ``1.0``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    @property
    def pathos(self) -> float:
        """Return the agent's internal energy calculated from emotion and tension."""
        return (self.emotion + self.tension) / 2

    def sync_pathos(self) -> None:
        """Synchronize internal energy with the current state.

        If ``pathos`` exceeds ``0.6`` a state transition is attempted.
        """
        if self.pathos > 0.6:
            self.transition()

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

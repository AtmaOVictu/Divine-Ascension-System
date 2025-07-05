class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current level of internal tension.
    emotion:
        Current emotion intensity.
    pathos:
        Cumulative internal energy influencing transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, pathos: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension and pathos."""
        self.emotion = value
        self.tension += value
        self.pathos += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level and adjust pathos."""
        self.tension = value
        self.pathos += value

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust internal pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def transition(self) -> str:
        """Perform state transition if emotion or tension thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def sync_pathos(self) -> str:
        """Synchronize pathos with state transitions when energy is high."""
        if self.pathos > 5:
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

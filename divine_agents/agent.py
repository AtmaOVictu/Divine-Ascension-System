class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The name of the agent.
    state:
        Ontological state of the agent. Defaults to ``"Ego"``.
    tension:
        Current tension level of the agent.
    emotion:
        Current emotion intensity of the agent.
    pathos:
        Internal energy driving automatic synchronisation. ``0`` by default.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, pathos: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def sync_pathos(self, external_factor: float) -> None:
        """Synchronize pathos with external influence and adjust tension."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0
        # Pathos increases tension subtly to drive transitions
        self.tension = min(1.0, self.tension + external_factor * 0.2)

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

        The response tone is affected by the current emotion level.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"Strastno pravi: {base}"
        return base

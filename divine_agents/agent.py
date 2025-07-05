class Agent:
    """Ontological agent capable of emotional transitions.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def adjust_emotion(self, delta: float) -> None:
        """Increment emotion by ``delta`` and adjust tension.

        Parameters
        ----------
        delta:
            Amount to add to the current emotion.
        """
        self.update_emotion(self.emotion + delta)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if tension or emotion are high."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.PRINCIPLES.get(self.state, "")

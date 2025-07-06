class Agent:
    """Ontological agent capable of transitioning philosophical states.

    States are driven by ``tension`` and ``emotion``. A transition occurs
    when ``tension`` is greater than ``0.7`` or ``emotion`` is greater than
    ``0.5``. The mapping of states to their symbolic representation is stored
    in ``STATE_SYMBOLS``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    STATE_SYMBOLS = {
        "Ego": "⊘",
        "Jaz": "∫(dru/x)",
        "Enotnost": "RES001",
    }

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

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    @property
    def symbol(self) -> str:
        """Return the ontological symbol for the current state."""
        return self.STATE_SYMBOLS[self.state]

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = "" if self.emotion < 0.5 else "(čustveno) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

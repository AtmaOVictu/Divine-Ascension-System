class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial tension value.
    emotion:
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        weight: float = 0.0,
        pressure: float = 0.0,
        quasi_potency: float = 0.0,
        definitive_share: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Additional metrics inspired by the philosophical model
        self.weight = weight
        self.pressure = pressure
        self.quasi_potency = quasi_potency
        self.definitive_share = definitive_share
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_weight(self, value: float) -> None:
        """Update weight of the emotion and modify tension."""
        self.weight = value
        self.tension += value

    def update_pressure(self, value: float) -> None:
        """Update dimensional pressure and modify tension."""
        self.pressure = value
        self.tension += value

    def update_quasi_potency(self, value: float) -> None:
        """Set the quasi potency value."""
        self.quasi_potency = value

    def update_definitive_share(self, value: float) -> None:
        """Set the definitive share value."""
        self.definitive_share = value

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."
        return f"{msg} (čustvo: {self.emotion:.1f}, napetost: {self.tension:.1f})"

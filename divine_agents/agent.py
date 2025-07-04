class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.last_cause = None

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def apply_force(self, force_type: str, value: float) -> None:
        """Apply an external or internal influence.

        Parameters
        ----------
        force_type: str
            One of ``"external"``, ``"internal"``, or ``"previous"`` to denote
            the origin of the influence.
        value: float
            Intensity of the influence.
        """
        if force_type == "external":
            self.update_tension(value)
        elif force_type == "internal":
            self.update_emotion(value)
        elif force_type == "previous":
            self.update_emotion(value * 0.5)
            self.update_tension(value * 0.5)
        else:
            raise ValueError("Invalid force type")

        self.last_cause = force_type

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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return base + " Čutim to zelo intenzivno."
        if self.emotion < 0.3:
            return base + " Govorim mirno."
        return base

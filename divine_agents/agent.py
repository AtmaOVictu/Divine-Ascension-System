from .integrity_box import IntegrityBox


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Every agent maintains an :class:`IntegrityBox` that stores its current
    state, tension and emotion values. Any modification to these attributes is
    performed through the box to keep a history of changes and allow integrity
    checks.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.box = IntegrityBox(name, {
            "state": state,
            "tension": tension,
            "emotion": emotion,
            "integrity_status": "valid",
        })

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.box.update_data({"emotion": self.emotion, "tension": self.tension})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.box.update_data({"tension": self.tension})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.box.update_data({"state": self.state})
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def check_integrity(self) -> str:
        """Expose box integrity status."""
        return self.box.check_integrity()

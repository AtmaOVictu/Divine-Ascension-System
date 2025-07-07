from .integrity import IntegrityBox


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        data = {"state": state, "tension": tension, "emotion": emotion, "integrity_status": "valid"}
        self.box = IntegrityBox(name, data)
        self.history = [state]

    @property
    def name(self) -> str:
        return self.box.name

    @property
    def state(self) -> str:
        return self.box.data["state"]

    @property
    def tension(self) -> float:
        return self.box.data["tension"]

    @property
    def emotion(self) -> float:
        return self.box.data["emotion"]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        new_tension = self.tension + value
        self.box.update_data({"emotion": value, "tension": new_tension})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.box.update_data({"tension": value})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        new_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                new_state = "Jaz"
            elif self.state == "Jaz":
                new_state = "Enotnost"
        self.box.transition({"state": new_state})
        self.history.append(new_state)
        return new_state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def check_integrity(self) -> str:
        """Expose the box integrity status."""
        return self.box.check_integrity()

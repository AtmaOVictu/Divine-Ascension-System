from .integrity import IntegrityBox


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.box = IntegrityBox(
            name,
            {
                "state": state,
                "tension": tension,
                "emotion": emotion,
            },
        )
        self.history = [state]

    @property
    def state(self) -> str:
        return self.box.data.get("state", "Ego")

    @property
    def tension(self) -> float:
        return self.box.data.get("tension", 0.0)

    @property
    def emotion(self) -> float:
        return self.box.data.get("emotion", 0.0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.box.update_data({"emotion": value, "tension": self.tension + value})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.box.update_data({"tension": value})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if state == "Ego":
                state = "Jaz"
            elif state == "Jaz":
                state = "Enotnost"
            if state != self.state:
                self.box.transition({"state": state})
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        state = self.state
        if state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

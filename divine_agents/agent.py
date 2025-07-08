from .frame import Frame


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.frame = Frame(state, tension, emotion)
        self.history = [self.frame]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.frame.emotion = value
        self.frame.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.frame.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.frame.tension > 0.7 or self.frame.emotion > 0.5:
            if self.frame.state == "Ego":
                self.frame = Frame("Jaz", self.frame.tension, self.frame.emotion)
            elif self.frame.state == "Jaz":
                self.frame = Frame("Enotnost", self.frame.tension, self.frame.emotion)
        self.history.append(self.frame)
        return self.frame.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.frame.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.frame.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # Expose state, tension, and emotion for convenience
    @property
    def state(self) -> str:
        return self.frame.state

    @property
    def tension(self) -> float:
        return self.frame.tension

    @property
    def emotion(self) -> float:
        return self.frame.emotion

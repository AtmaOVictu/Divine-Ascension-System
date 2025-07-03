class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class SelfDeceptionAgent(Agent):
    """Agent that can rationalize to avoid state transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, deception_threshold: float = 0.9):
        super().__init__(name, state, tension, emotion)
        self.deception_threshold = deception_threshold
        self.rationalizations = []

    def rationalize(self) -> str:
        """Create a rationalization to maintain the current state."""
        message = "Ni potrebe po spremembi, ker je tako varneje."
        self.rationalizations.append(message)
        return message

    def transition(self) -> str:
        """Override transition to allow self-deception to halt progress."""
        if (self.tension > 0.7 or self.emotion > 0.5) and (
            self.tension < self.deception_threshold and
            self.emotion < self.deception_threshold
        ):
            # Create rationalization and remain in current state
            self.rationalize()
            self.history.append(self.state)
            return self.state
        return super().transition()

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, opposite: float = 0.0):
        """Initialize agent with optional opposite (contradiction) value."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.opposite = opposite
        self.history = [state]

    def update_emotion(self, value: float, opposite: float = 0.0) -> None:
        """Update emotion and its opposite, adjusting tension accordingly."""
        self.emotion = value
        self.opposite = opposite
        self.tension += value + opposite

    def update_opposite(self, value: float) -> None:
        """Update the opposite value directly and adjust tension."""
        self.opposite = value
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

    def get_state(self):
        """Return a tuple with tension, emotion and opposite values."""
        return self.tension, self.emotion, self.opposite

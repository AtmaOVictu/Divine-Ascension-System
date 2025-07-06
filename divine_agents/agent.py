class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        origin: str = "O",
        opposites: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.origin = origin
        self.tension = tension
        self.emotion = emotion
        self.opposites: dict[str, str] = opposites or {}
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def set_opposite(self, opposite: str) -> None:
        """Assign an opposite concept for the current state."""
        self.opposites[self.state] = opposite

    def get_opposite(self) -> str:
        """Return the opposite concept for the current state if defined."""
        return self.opposites.get(self.state, "")

    def display_state(self) -> str:
        """Return a textual representation of the current state and its opposite."""
        opposite = self.get_opposite()
        return f"{self.state}{f' (opposite: {opposite})' if opposite else ''}"

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

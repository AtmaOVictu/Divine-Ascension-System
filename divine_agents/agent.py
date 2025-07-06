class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent maintains a link to the fundamental ``O`` (origin state) and can
    hold opposite concepts for any given ontological state.  Transitions are
    triggered when either the ``tension`` exceeds ``0.7`` or ``emotion`` exceeds
    ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        base: str = "O",
        opposites: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.base = base
        self.opposites: dict[str, str] = opposites or {}
        self.history = [state]

    def set_opposite(self, opposite: str, state: str | None = None) -> None:
        """Associate an opposite concept with a state (defaults to current)."""
        key = state or self.state
        self.opposites[key] = opposite

    def get_opposite(self, state: str | None = None) -> str | None:
        """Retrieve the opposite concept for a state (defaults to current)."""
        key = state or self.state
        return self.opposites.get(key)

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

    def display_state(self) -> str:
        """Human readable presentation of current state and its opposite."""
        opposite = self.get_opposite() or "None"
        return f"{self.name} is in state {self.state} with opposite {opposite}."

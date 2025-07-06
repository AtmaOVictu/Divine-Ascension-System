class Agent:
    """Ontological agent capable of transitioning states.

    The agent maintains an optional mapping of opposite concepts and keeps
    a connection to the base ontological element ``O`` which represents a
    stable starting point for all transitions.
    """

    O = "O"  # base state representing stability
    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, opposites=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.opposites = opposites or {}

    def set_opposite(self, opposite: str) -> None:
        """Assign an opposite concept for the agent's current state."""
        self.opposites[self.state] = opposite

    def get_opposite(self) -> str:
        """Return the opposite concept for the current state if available."""
        return self.opposites.get(self.state, "None")

    def display_state(self) -> str:
        """Return a human readable description of the current state."""
        opposite = self.get_opposite()
        return f"{self.name} is in state {self.state} with opposite {opposite}."

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

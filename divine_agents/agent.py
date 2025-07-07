"""Core agent logic for ontological transitions."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, rationality: float = 1.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.rationality = rationality
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_rationality(self, value: float) -> None:
        """Update rationality level."""
        self.rationality = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (self.tension > 0.7 or self.emotion > 0.5) and self.rationality > 0.5:
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

    def reflect_opposites(self) -> str:
        """Reflect on opposites according to the current state."""
        if self.state == "Ego":
            return f"{self.name}: I am independent, yet I must face others."
        if self.state == "Jaz":
            return f"{self.name}: I am in relation with others, yet struggle to retain myself."
        return f"{self.name}: I am unified, yet the duality within me remains."

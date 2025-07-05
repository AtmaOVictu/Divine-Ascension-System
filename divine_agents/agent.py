class Agent:
    """Ontological agent capable of transitioning states and dimensions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, dimension: int = 1):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.dimension = dimension
        self.senses = {"touch": 0.0, "sight": 0.0}
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_dimension(self, value: int) -> None:
        """Set the current dimension."""
        self.dimension = value

    def compute_senses(self) -> dict:
        """Calculate sense influence based on current emotion."""
        self.senses["touch"] = self.emotion * 0.5
        self.senses["sight"] = self.emotion * 0.4
        return self.senses

    def dimension_influence(self) -> float:
        """Return influence percentage for the current dimension."""
        return self.emotion * self.dimension

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
                self.dimension = 2
            elif self.state == "Jaz":
                self.state = "Enotnost"
                self.dimension = 3
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

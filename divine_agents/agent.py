class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, potence: float = 1.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.potence = potence
        self.connections = []
        self.history = [state]

    def connect(self, other: "Agent") -> None:
        """Record knowledge of another agent."""
        if other is not self and other not in self.connections:
            self.connections.append(other)

    def share_potence(self, other: "Agent") -> float:
        """Multiply potence with another agent to represent connection."""
        self.connect(other)
        return self.potence * other.potence

    def divide_potence(self, other: "Agent") -> float:
        """Divide potence by another agent's potence."""
        self.connect(other)
        if other.potence == 0:
            return float('inf')
        return self.potence / other.potence

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

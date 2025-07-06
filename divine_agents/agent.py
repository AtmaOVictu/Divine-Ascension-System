class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent with optional initial state, tension and emotion."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # history keeps track only of state changes
        self.history = [state]

    def update_emotion(self, change: float) -> None:
        """Increase emotion by ``change`` and raise tension accordingly."""
        self.emotion = max(0.0, min(1.0, self.emotion + change))
        self.tension = max(0.0, min(1.0, self.tension + change))

    def update_tension(self, change: float) -> None:
        """Increase tension by ``change`` keeping it within [0, 1]."""
        self.tension = max(0.0, min(1.0, self.tension + change))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if self.state != previous:
            self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

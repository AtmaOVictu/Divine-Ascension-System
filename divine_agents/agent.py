class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize a new agent with optional starting values."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep track of every state the agent has been in
        self.history = [state]

    def update_emotion(self, change: float) -> None:
        """Increase emotion by ``change`` and update tension."""
        self.emotion = max(0.0, min(1.0, self.emotion + change))
        # higher emotion slightly raises tension
        self.update_tension()

    def update_tension(self) -> None:
        """Increase tension based on current emotion."""
        self.tension = max(0.0, min(1.0, self.tension + self.emotion / 10))

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

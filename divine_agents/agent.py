class Agent:
    """Represents an ontological agent capable of state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    # ------------------------------------------------------------------
    # Update helpers
    # ------------------------------------------------------------------
    def update_emotion(self, delta: float) -> None:
        """Increase emotion and tension simultaneously."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.tension = max(0.0, min(1.0, self.tension + delta))

    def update_tension(self, delta: float) -> None:
        """Adjust tension without touching emotion."""
        self.tension = max(0.0, min(1.0, self.tension + delta))

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def philosophy(self) -> str:
        """Return the statement that reflects the agent's current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base

    def respond(self, question: str) -> str:
        """Generate a philosophical response influenced by emotion."""
        statement = self.philosophy()
        if self.emotion >= 0.5:
            statement += " Čutim močna čustva, kar poglablja mojo misel."
        elif self.emotion > 0.0:
            statement += " Čutim rahla čustva, ki barvajo moje besede."
        return statement

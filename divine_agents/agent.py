class Agent:
    """Represents an ontological agent capable of transitioning states and phases."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, phase: int = 1):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.phase = phase
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # -------------------------------
    # Phase manipulation operations
    # -------------------------------

    def evolve(self) -> int:
        """Move the agent one phase forward."""
        if self.phase < 100:
            self.phase += 1
        return self.phase

    def permute(self, shift: int = 1) -> int:
        """Change the current phase by ``shift`` within the allowed range."""
        self.phase = max(1, min(100, self.phase + shift))
        return self.phase

    def degrade(self) -> int:
        """Move the agent one phase backward if possible."""
        if self.phase > 1:
            self.phase -= 1
        return self.phase

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

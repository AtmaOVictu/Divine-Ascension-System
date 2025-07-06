class Agent:
    """Represents an ontological agent capable of transitioning states."""

    #: Ontological states represented with greek symbols for clarity
    STATES = ("Ε", "Ψ", "Ω")

    def __init__(self, name: str, state: str = "Ε", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        # Store the current ontological state as a greek symbol
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def __str__(self) -> str:
        return f"{self.name} ({self.state}): Tension={self.tension}, Emotion={self.emotion}"

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
            if self.state == "Ε":
                self.state = "Ψ"
            elif self.state == "Ψ":
                self.state = "Ω"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ε":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Ψ":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    # Ontological state symbols
    EGO = "Ε"
    JAZ = "Ψ"
    ENOTNOST = "Ω"

    STATES = (EGO, JAZ, ENOTNOST)

    def __init__(self, name: str, state: str = EGO, tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

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
            if self.state == self.EGO:
                self.state = self.JAZ
            elif self.state == self.JAZ:
                self.state = self.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == self.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == self.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

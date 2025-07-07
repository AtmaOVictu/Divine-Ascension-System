class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.balality_history = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if previous != self.state:
            self.balality_history.append((previous, self.state))
        self.history.append(self.state)
        return self.state

    def reflect_balality(self) -> str:
        """Return a statement about the most recent balality."""
        if not self.balality_history:
            return f"{self.name}: Balality has yet to emerge."
        prev, current = self.balality_history[-1]
        if current == "Jaz":
            return (
                f"{self.name}: Moving from {prev} to {current}, "
                "resnica postaja relativna."
            )
        if current == "Enotnost":
            return (
                f"{self.name}: From {prev} to {current}, "
                "cutim povezanost vseh resnic."
            )
        return f"{self.name}: {current} ostaja v ravnovesju z nasprotjem."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
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
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        prefix = "Mirno:" if self.emotion <= 0.5 else "Strastno:"
        if self.state == "Ego":
            view = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            view = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            view = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {view}"

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
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def feel(self, delta: float) -> None:
        """Increase emotion and tension gradually."""
        self.update_emotion(self.emotion + delta)
        self.update_tension(min(1.0, self.tension + delta))

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
        """Return a philosophical answer influenced by the current state."""
        tone = "Mirno" if self.emotion < 0.3 else "Strastno" if self.emotion < 0.7 else "Silovito"
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{tone}: {base}"


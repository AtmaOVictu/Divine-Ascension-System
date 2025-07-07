class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create an agent with the given initial state, tension and emotion."""
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

    def state_principle(self) -> str:
        """Return the philosophical principle of the current state."""
        principles = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        return principles[self.state]

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self.state_principle()
        if self.emotion > 0.6:
            suffix = " (čustveno odziven)"
        elif self.emotion > 0.2:
            suffix = " (rahlo čustven)"
        else:
            suffix = ""
        return base + suffix

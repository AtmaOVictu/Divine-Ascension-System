class Agent:
    """Ontological agent capable of transitioning through philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent with an initial state, tension, and emotion."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and increase tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the tension level explicitly."""
        self.tension = value

    def transition(self) -> str:
        """Move to the next state when emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer shaped by state and emotion."""
        base = self.PRINCIPLES[self.state]
        if self.emotion > 0.5:
            return f"(Čustveno) {base}"
        return base

class Agent:
    """Ontological agent that transitions states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state if state in self.STATES else "Ego"
        self.tension = tension
        self.emotion = emotion
        self.history = [self.state]

    def update_emotion(self, delta: float) -> float:
        """Update emotion intensity in a 0-1 cycle and adjust tension."""
        self.emotion = (self.emotion + delta) % 1.0
        self.tension += delta
        return self.emotion

    def update_tension(self, value: float) -> float:
        """Directly set tension level."""
        self.tension = value
        return self.tension

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _principle(self) -> str:
        """Return base philosophical statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self._principle()
        if self.emotion > 0.7:
            return f"{base} Čutim intenzivna čustva."
        if self.emotion > 0.3:
            return f"{base} Čustveno sem vznemirjen."
        return base

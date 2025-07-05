class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def philosophical_principle(self) -> str:
        """Return the principle associated with the current state."""
        return self.PRINCIPLES[self.state]

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
        """Return a philosophical answer depending on state and emotion."""
        base = self.philosophical_principle()
        if self.emotion > 0.7:
            mood = "z močnimi čustvi"
        elif self.emotion > 0.3:
            mood = "rahlo čustveno"
        else:
            mood = "mirno"
        return f"{mood}: {base}"

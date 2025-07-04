class Agent:
    """Ontological agent capable of emotional transitions and dialogue."""

    STATES = ("Ego", "Jaz", "Enotnost")
    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str | None = None) -> None:
        """Create a new agent with a given ontological state."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, emotion_name: str, intensity: float) -> None:
        """Update emotion and adjust tension based on intensity."""
        self.emotion_name = emotion_name
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def philosophical_principle(self) -> str:
        """Return the philosophical principle of the current state."""
        return self.PRINCIPLES[self.state]

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        principle = self.philosophical_principle()
        if self.emotion_name:
            return f"({self.emotion_name}) {principle}"
        return principle

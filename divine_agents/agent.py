class Agent:
    """Represents an ontological agent capable of transitioning ontological states."""

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

    def update_emotion(self, value: float) -> None:
        """Set a new emotion level and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = min(1.0, self.tension + self.emotion)

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

    def _emotion_prefix(self) -> str:
        if self.emotion > 0.7:
            return "Z intenzivnimi čustvi"
        if self.emotion > 0.4:
            return "S čustvi"
        return "Mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        base = self.PRINCIPLES.get(self.state, "")
        return f"{self._emotion_prefix()}: {base}"

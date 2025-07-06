class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, experiences=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.experiences = experiences or []

    def add_experience(self, exp: str) -> None:
        """Store a new experience affecting future transitions."""
        self.experiences.append(exp)

    def update_history(self) -> None:
        """Record the current state into history."""
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5 or self._historical_trigger():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.update_history()
        return self.state

    def _historical_trigger(self) -> bool:
        """Return True if past experiences force a transition."""
        if "self-preservation" in self.experiences and self.state == "Ego":
            return True
        if "altruistic" in self.experiences and self.state == "Jaz":
            return True
        return False

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

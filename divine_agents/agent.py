class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Meditative")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self._previous_state = None

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def enter_meditative(self) -> None:
        """Enter a temporary meditative state reducing tension and emotion."""
        if self.state != "Meditative":
            self._previous_state = self.state
            self.state = "Meditative"
            self.history.append(self.state)

    def meditative_step(self, reduction: float = 0.1) -> str:
        """Reduce tension and emotion while in meditative state."""
        if self.state == "Meditative":
            self.tension = max(0.0, self.tension - reduction)
            self.emotion = max(0.0, self.emotion - reduction)
            if self.tension == 0.0 and self.emotion == 0.0:
                self.state = self._previous_state or "Ego"
                self._previous_state = None
                self.history.append(self.state)
        return self.state

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.state == "Meditative":
            return self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

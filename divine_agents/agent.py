class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Emotion values must be non-negative and are capped at 1.0. Tension is
        increased by the emotion value but also capped within ``[0.0, 1.0]``.
        """
        if value < 0:
            raise ValueError("Emotion value cannot be negative")
        self.emotion = min(value, 1.0)
        self.tension = min(max(self.tension + self.emotion, 0.0), 1.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Tension values must be non-negative and are capped at 1.0.
        """
        if value < 0:
            raise ValueError("Tension value cannot be negative")
        self.tension = min(value, 1.0)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if self.state != previous_state:
            self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

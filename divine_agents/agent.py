class Agent:
    """Represent an ontological agent capable of transitioning between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion to ``value`` and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def feel(self, delta: float) -> None:
        """Increment emotion by ``delta`` and update tension gradually."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.update_tension()

    def update_tension(self, value: float | None = None) -> None:
        """Update tension directly or evolve it from current emotion.

        If ``value`` is provided, tension is set to that value. Otherwise the
        tension slowly increases based on the current emotion, simulating a
        feedback loop from past interactions.
        """
        if value is not None:
            self.tension = value
        else:
            self.tension += (self.emotion / 10) * 0.9
        self.tension = max(0.0, min(1.0, self.tension))

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

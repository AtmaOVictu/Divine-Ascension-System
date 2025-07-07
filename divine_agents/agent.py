"""Ontological agents capable of state transitions and reinforcement."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [("init", state, tension, emotion)]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.history.append(("emotion_update", self.state, self.tension, self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.history.append(("tension_update", self.state, self.tension, self.emotion))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(("transition", self.state, self.tension, self.emotion))
        return self.state

    def reward(self, result: bool) -> None:
        """Reinforce agent behaviour based on success or failure."""
        if result:
            self.emotion += 0.1
        else:
            self.emotion -= 0.1
        self.history.append(("reward", self.state, self.tension, self.emotion))

    def respond(self, question: str) -> str:
        """Return a philosophical answer with emotional context."""
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih. (čustvo: {self.emotion:.2f})"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi. (čustvo: {self.emotion:.2f})"
        return f"Vse resnice so eno, medsebojno povezane. (čustvo: {self.emotion:.2f})"

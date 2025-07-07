class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [(state, tension, emotion)]

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
        """Reinforce agent behavior based on success."""
        if result:
            self.emotion += 0.1
        else:
            self.emotion -= 0.1
        self.history.append(("reward", self.state, self.tension, self.emotion))

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        self.history.append(("respond", self.state, self.tension, self.emotion))
        return f"{answer} (čustvo: {self.emotion:.2f})"

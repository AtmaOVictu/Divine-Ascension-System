class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 love: float = 0.0, hate: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.love = love
        self.hate = hate
        self.history = [state]

    def update_emotion(self) -> None:
        """Update emotional state using love and hate values."""
        self.emotion = self.love - self.hate
        self.tension += abs(self.emotion)
        self.history.append(f"Emotion updated to: {self.emotion}")

    def update_love(self, value: float) -> None:
        """Set love level and refresh emotion."""
        self.love = value
        self.update_emotion()

    def update_hate(self, value: float) -> None:
        """Set hate level and refresh emotion."""
        self.hate = value
        self.update_emotion()

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

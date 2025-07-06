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

    def emotion_label(self) -> str:
        """Return a simple textual label for the current emotion value."""
        if self.emotion > 0.7:
            return "veselje"
        if self.emotion > 0.4:
            return "nemir"
        return "mirnost"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        label = self.emotion_label()
        if self.state == "Ego":
            return f"({label}) Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"({label}) Resnica je relativna, oblikovana z nasimi odnosi."
        return f"({label}) Vse resnice so eno, medsebojno povezane."

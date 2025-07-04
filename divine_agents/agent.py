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

    def emotion_descriptor(self) -> str:
        """Return a textual description of the current emotion level."""
        if self.emotion > 0.7:
            return "z intenzivnimi čustvi"
        if self.emotion > 0.5:
            return "s čustveno napetostjo"
        return "mirno"

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
        prefix = self.emotion_descriptor()
        if self.state == "Ego":
            philosophy = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            philosophy = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            philosophy = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {philosophy}"

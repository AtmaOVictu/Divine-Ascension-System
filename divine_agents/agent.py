class Agent:
    """Represents an ontological agent capable of transitioning states."""

    #: Ordered list of possible states
    STATES = ("0", "1", "Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "0", tension: float = 0.0, emotion: float = 0.0):
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
            if self.state == "0":
                self.state = "1"
            elif self.state == "1":
                self.state = "Ego"
            elif self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "0":
            return "Začetek: potencial še ni izpolnjen."
        if self.state == "1":
            return "Prvi korak: enotnost se oblikuje iz potenciala."
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

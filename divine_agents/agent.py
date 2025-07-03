class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Nasprotje")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension = min(self.tension + value, 1.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(value, 2.0))

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
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = ""
        if self.emotion > 0.7:
            prefix = "Močno čutim, da "
        if self.state == "Ego":
            return f"{prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return f"{prefix}Vse resnice so eno, medsebojno povezane."
        return f"{prefix}Nasprotja združujejo resnico."

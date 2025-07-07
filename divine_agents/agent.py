class Agent:
    """Represents an ontological agent capable of evolving or devolving states."""

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
        """Perform state transition based on current emotion and tension."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.evolve()
        elif self.tension < 0.3 or self.emotion < 0.3:
            self.devolve()
        self.history.append(self.state)
        return self.state

    def evolve(self) -> str:
        """Progress to a more complex ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        return self.state

    def devolve(self) -> str:
        """Return to a previous ontological state."""
        if self.state == "Enotnost":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Ego"
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

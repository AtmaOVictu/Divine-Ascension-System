class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "RES000", "RES010", "Jaz", "Enotnost")

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
        """Perform state transition with intermediate RES000 and RES010 states."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "RES000"
            elif self.state == "RES000":
                self.state = "RES010"
            elif self.state == "RES010":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "RES000":
            return "Dosegel sem stabilnost, resnica odseva notranji mir."
        if self.state == "RES010":
            return "Sem v prehodni fazi, kjer se resnica kristalizira."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def __str__(self) -> str:
        return f"Agent {self.name} je v stanju: {self.state}, zgodovina: {self.history}"

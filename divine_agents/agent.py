class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.EMOTIONS = {
            'fear': 0.3,
            'joy': 0.7,
            'anger': 0.5,
        }

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def evolve(self) -> str:
        """Progress to a higher state when emotion or tension exceed thresholds."""
        return self.transition()

    def devolve(self) -> str:
        """Regress to a previous state when emotion intensity drops."""
        if self.emotion < 0.3:
            if self.state == "Enotnost":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Ego"
        self.history.append(self.state)
        return self.state

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
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."
        return f"{truth} Čustvo: {self.emotion:.2f}"

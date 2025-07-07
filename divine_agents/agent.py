class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Initialize the agent with a starting state, tension and emotion."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(self.emotion + value, 1.0))
        self.tension = max(0.0, min(self.tension + value, 1.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(value, 1.0))

    def transition(self) -> str:
        """Perform state transition if tension or emotion exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        if self.state == "Ego":
            statement = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            prefix = "Burno: "
        elif self.emotion > 0.3:
            prefix = "Strastno: "
        else:
            prefix = "Umirjeno: "
        return f"{prefix}{statement}"

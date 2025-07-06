class Agent:
    """Ontological agent that transitions through philosophical states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting ontological state. Defaults to ``"Ego"``.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name: str = name
        self.state: str = state
        self.tension: float = tension
        self.emotion: float = emotion
        self.history: list[str] = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_influence(self, delta: float) -> None:
        """Increment emotion and tension by a given amount."""
        self.update_emotion(min(1.0, self.emotion + delta))

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

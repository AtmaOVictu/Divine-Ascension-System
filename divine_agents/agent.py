class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Initial tension level.
    emotions: dict, optional
        Mapping of emotion name to its intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        if state not in self.STATES:
            raise ValueError(f"Unknown state '{state}'")
        self.state = state
        self.tension = tension
        self.emotions = emotions or {e: 0.0 for e in self.EMOTIONS}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion intensity and recompute tension."""
        if name not in self.emotions:
            raise ValueError(f"Unknown emotion '{name}'")
        self.emotions[name] = value
        self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        peak_emotion = max(self.emotions.values(), default=0.0)
        if self.tension > 0.7 or peak_emotion > 0.5:
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

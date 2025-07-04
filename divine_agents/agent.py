class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Human readable name of the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Accumulated tension influencing transitions.
    emotion: float
        Current emotional intensity. Higher values increase tension.
    history: List[str]
        Chronological record of states after each transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    RESPONSES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotional intensity and automatically adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.tension > self.THRESHOLD_TENSION
            or self.emotion > self.THRESHOLD_EMOTION
        ):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.RESPONSES.get(self.state, "")

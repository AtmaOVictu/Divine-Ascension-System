class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Agent identifier.
    state : str
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension : float
        Level of internal tension influencing transitions.
    emotion : float
        Intensity of current emotion. Values above ``0.5`` may trigger
        transitions.
    history : list[str]
        List of states the agent has traversed.
    """

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

    def describe_emotion(self) -> str:
        """Return a textual description of the current emotional state."""
        if self.emotion > 0.7:
            return "v strasti"
        if self.emotion > 0.4:
            return "čustveno"
        return "mirno"

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
        mood = self.describe_emotion()
        if self.state == "Ego":
            return f"{mood}: Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{mood}: Resnica je relativna, oblikovana z našimi odnosi."
        return f"{mood}: Vse resnice so eno, medsebojno povezane."

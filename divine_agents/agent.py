class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name : str
        Unique identifier for the agent.
    state : str, optional
        Ontological phase (one of ``Ego``, ``Jaz``, ``Enotnost``).
        Defaults to ``"Ego"``.
    tension : float, optional
        Internal stress level on a ``0.0``-``1.0`` scale. Defaults to ``0.0``.
        Values above ``0.7`` may trigger a state change.
    emotion : float, optional
        Emotional intensity on a ``0.0``-``1.0`` scale. Defaults to ``0.0``.
        Values above ``0.5`` may trigger a state change.
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

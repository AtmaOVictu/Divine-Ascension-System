class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Starting ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current level of tension influencing transitions.
    emotion:
        Intensity of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = "neutral"
        self.history = [state]

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity and name, adjusting tension accordingly."""
        self.emotion = value
        self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` -> ``Jaz`` -> ``Enotnost`` when either
        :pyattr:`tension` exceeds ``0.7`` or :pyattr:`emotion` exceeds ``0.5``.
        """
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

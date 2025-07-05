class Agent:
    """Ontological agent that transitions between philosophical states.

    Parameters
    ----------
    name:
        Human readable identifier of the agent.
    state:
        Current ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Numeric representation of the agent's inner tension.
    emotion:
        Intensity of the current emotional state.
    emotion_name:
        Human readable description of the current emotion (e.g. ``fear``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = ""):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        name:
            Name of the emotion (e.g. ``fear`` or ``joy``).
        value:
            Intensity of the emotion in the ``0-1`` range.
        """
        self.emotion_name = name
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
        """Return a philosophical answer influenced by the current state."""
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name:
            return f"[{self.emotion_name}] {msg}"
        return msg

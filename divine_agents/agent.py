class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique identifier for the agent.
    state:
        Ontological phase the agent starts in. One of ``Ego``, ``Jaz`` or
        ``Enotnost``.
    tension:
        Current level of tension influencing state transitions.
    emotion:
        Intensity of the current emotion.
    emotion_type:
        Type of the current emotion (e.g. ``fear``, ``joy``, ``anger``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension.

        Parameters
        ----------
        emotion_type:
            Name of the emotion to set.
        value:
            Intensity of the emotion in range 0--1.
        """
        self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value in range 0--1.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        Returns
        -------
        str
            The new state after transition.
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
        prefix = f"({self.emotion_type}) " if self.emotion_type else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Numeric value representing internal tension. Values above ``0.7`` may
        trigger a state transition.
    emotion:
        Numeric intensity of the current emotion. Values above ``0.5`` may
        trigger a state transition.
    emotion_type:
        Label of the current dominant emotion (e.g. ``fear``, ``joy`` or
        ``anger``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity in the ``0-1`` range.
        emotion_type:
            Optional label for the emotion (e.g. ``fear``). When provided the
            internal ``emotion_type`` attribute is updated.
        """
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent will move from ``Ego`` to ``Jaz`` or from ``Jaz`` to
        ``Enotnost`` when ``tension`` exceeds ``0.7`` or ``emotion`` exceeds
        ``0.5``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The wording is slightly influenced by the agent's current
        ``emotion_type``.
        """
        prefix = f"Občutim {self.emotion_type}: " if self.emotion_type != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

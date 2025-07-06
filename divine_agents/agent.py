class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Initial ontological state of the agent. Defaults to ``"Ego"``.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    emotion_label:
        Human readable label describing the current dominant emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity and label and adjust tension.

        Parameters
        ----------
        value:
            New emotion intensity in the range ``0.0`` - ``1.0``.
        label:
            Descriptive label of the emotion (e.g. ``"fear"``).
        """
        self.emotion = value
        self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        when either :pyattr:`tension` is greater than ``0.7`` or
        :pyattr:`emotion` is greater than ``0.5``.
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

        The returned string also reflects the agent's current dominant emotion
        if set.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label and self.emotion_label != "neutral":
            return f"{base} (Čutim {self.emotion_label}.)"
        return base

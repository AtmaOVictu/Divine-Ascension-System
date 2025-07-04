class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Human readable identifier of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial level of inner tension.
    emotion:
        Initial emotion intensity. Higher values increase tension and may trigger
        state transitions.
    emotion_type:
        Optional descriptor of the current emotion (e.g. ``"fear"`` or
        ``"joy"``).  It does not influence transitions directly but is reported
        in responses.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity. The same value is added to ``tension``.
        kind:
            Optional descriptor of the emotion (e.g. ``"fear"``).  When
            provided it will replace :attr:`emotion_type`.
        """
        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
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
        """Return a philosophical answer depending on the current state and emotion."""
        mood = ""
        if self.emotion > 0.5:
            mood = " Čutim močna čustva." if self.emotion_type is None else f" Čutim {self.emotion_type}."
        elif self.emotion > 0.0:
            mood = " Moja čustva so umirjena."

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return base + mood

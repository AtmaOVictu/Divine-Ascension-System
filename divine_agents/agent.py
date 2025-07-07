class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str
        Ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Current tension level in the interval ``[0, 1]``.
    emotion: float
        Current emotion intensity in the interval ``[0, 1]``.
    emotion_type: str
        Type of the dominating emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally change emotion type.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_type:
            Optional new emotion descriptor.
        """
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Convenience method to set both emotion type and intensity."""
        self.emotion_type = emotion_type
        self.update_emotion(value)

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
        prefix = ""
        if self.emotion > 0.5:
            match self.emotion_type:
                case "fear":
                    prefix = "S strahom"  # "With fear"
                case "anger":
                    prefix = "Z jezo"  # "With anger"
                case "joy":
                    prefix = "Z veseljem"  # "With joy"
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {base}".strip()

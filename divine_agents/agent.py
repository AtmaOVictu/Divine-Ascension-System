class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state. Defaults to ``"Ego"``.
    tension:
        Initial tension level. Defaults to ``0.0``.
    emotion:
        Initial emotion intensity. Defaults to ``0.0``.
    emotion_name:
        Descriptive name of the emotion (e.g. ``"fear"``). Defaults to
        ``"neutral"``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update emotion and adjust tension.

        Parameters
        ----------
        name:
            Descriptive name of the emotion (e.g. ``"fear"``).
        intensity:
            Numerical intensity of the emotion. ``0`` represents neutral.
        """

        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer influenced by emotion and state."""

        emotion_prefix = {
            "fear": "V strahu pravim:",
            "joy": "Z veseljem pravim:",
            "anger": "Z jezo pravim:",
        }.get(self.emotion_name, "")

        if self.state == "Ego":
            statement = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {statement}".strip()

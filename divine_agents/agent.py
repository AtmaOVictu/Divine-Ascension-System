class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial tension level.
    emotion:
        Intensity of the current emotion.
    emotion_type:
        Name of the emotion (e.g. ``"fear"``, ``"joy"``).  Used when
        forming responses and adjusting tension.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
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
            New emotion intensity in the range ``[0, 1]``.
        emotion_type:
            Optional name of the emotion influencing the agent.  If the
            emotion is ``"fear"`` or ``"anger"`` the tension is slightly
            increased to reflect heightened stress.
        """

        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type

        self.tension += value
        if self.emotion_type in {"fear", "anger"}:
            self.tension += 0.1

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
        """Return a philosophical answer influenced by state and emotion."""

        prefixes = {
            "fear": "V strahu povem, ",
            "anger": "Z jezo trdim, ",
            "joy": "Z veseljem pravim, ",
        }
        prefix = prefixes.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base

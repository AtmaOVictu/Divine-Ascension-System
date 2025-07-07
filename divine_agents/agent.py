class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            Intensity of the emotion on a scale from 0 to 1.
        name : str
            Name of the emotion (e.g., "fear", "joy").
        """
        self.emotion = value
        self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        whenever ``tension`` is greater than ``0.7`` or ``emotion`` exceeds
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
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_prefix = {
            "fear": "V strahu pravim: ",
            "joy": "Z veseljem pravim: ",
            "anger": "Z jezo pravim: ",
            "sorrow": "S žalostjo pravim: ",
            "neutral": "",
        }.get(self.emotion_name, "")

        return f"{emotion_prefix}{base}"

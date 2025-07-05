class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state ("Ego", "Jaz", or "Enotnost").
    tension: float
        Current tension level influencing transitions.
    emotion: float
        Intensity of the current emotion in range ``0-1``.
    emotion_type: str
        Type of the emotion (e.g. ``fear``, ``joy``, ``anger``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity.
        emotion_type: str, optional
            Type of the emotion (``fear``, ``joy``, ``anger`` or ``neutral``).
        """
        self.emotion = value
        self.emotion_type = emotion_type
        # Negative emotions increase tension more prominently
        if emotion_type in {"fear", "anger"}:
            self.tension += value
        else:
            self.tension += value / 2

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
        """Return a philosophical answer depending on state and emotion."""
        emotion_prefix = {
            "fear": "V strahu pravim:",
            "joy": "Z veseljem povem:",
            "anger": "Z jezo trdim:",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}".strip()

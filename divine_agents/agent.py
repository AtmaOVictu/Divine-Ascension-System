class Agent:
    """Ontological agent capable of transitioning states.

    Parameters
    ----------
    name : str
        Name of the agent.
    state : str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension : float, optional
        Initial tension level in the range ``0..1``.
    emotion : float, optional
        Initial emotional intensity in the range ``0..1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type: str | None = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotional state and adjust tension.

        Parameters
        ----------
        emotion_type : str
            Name of the current emotion (e.g. ``"fear"`` or ``"joy"``).
        intensity : float
            Intensity in the range ``0..1``.
        """
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (self.tension > 0.7 or self.emotion > 0.5) and self.state != "Enotnost":
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_phrase = {
            "fear": " Preveva me strah.",
            "joy": " Čutim radost.",
            "anger": " Preveva me jeza.",
        }.get(self.emotion_type, "")

        return base + emotion_phrase

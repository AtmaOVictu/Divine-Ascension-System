class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Initial tension level.
    emotion_label:
        Name of the current emotion (e.g. ``"fear"``).
    emotion_intensity:
        Intensity of the current emotion. This value also contributes to
        ``tension`` when updated.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_label: str = "neutral",
        emotion_intensity: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_label = emotion_label
        self.emotion_intensity = emotion_intensity
        self.history = [state]

    def update_emotion(self, label: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion_label = label
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
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

        prefix = ""
        if self.emotion_label == "fear":
            prefix = "S strahom "
        elif self.emotion_label == "joy":
            prefix = "Z veseljem "
        elif self.emotion_label == "anger":
            prefix = "Z jezo "

        return f"{prefix}{base}"

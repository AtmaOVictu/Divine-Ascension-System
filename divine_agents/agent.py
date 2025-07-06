class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    emotion_type:
        Type of emotion such as ``fear`` or ``joy``. Defaults to ``neutral``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion type and intensity while adjusting tension."""
        self.emotion_type = name
        self.update_emotion(intensity)

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
        """Return a philosophical answer based on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = {
            "fear": "S strahom",
            "joy": "Z veseljem",
            "anger": "Z jezo",
        }.get(self.emotion_type, "").strip()

        return f"{prefix + ': ' if prefix else ''}{base}"

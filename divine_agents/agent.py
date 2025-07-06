class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Agent identifier.
    state: str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Starting tension level.
    emotion: float, optional
        Intensity of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set an emotion and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    # Backwards compatibility
    def update_emotion(self, value: float) -> None:
        """Alias for :meth:`set_emotion` when emotion type is irrelevant."""
        self.set_emotion("", value)

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
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion_type:
            return f"[{self.emotion_type}] {base}"
        return base

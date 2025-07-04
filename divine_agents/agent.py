class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Internal tension value.
    emotion:
        Intensity of the current emotion.
    emotion_type:
        Optional label describing the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }
    EMOTION_PREFIX = {
        "fear": "S strahom odgovarjam:",
        "joy": "Z veseljem pravim:",
        "anger": "Z jezo pravim:",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        Emotional state influences how the answer is delivered.
        """
        base = self.PHILOSOPHY.get(self.state, "")
        prefix = self.EMOTION_PREFIX.get(self.emotion_type, "")
        return f"{prefix} {base}".strip()

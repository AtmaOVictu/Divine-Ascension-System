class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    a numeric ``tension`` level and an ``emotion`` value.  In addition to the
    numeric emotion intensity an optional ``emotion_type`` can be specified
    (e.g. ``"fear"`` or ``"joy"``).  State transitions only occur when the
    tension or emotion intensity exceed their respective thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, *, emotion_type: str | None = None) -> None:
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
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type != "neutral":
            return f"({self.emotion_type}) {base}"
        return base

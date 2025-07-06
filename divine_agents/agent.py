class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent maintains an ontological ``state`` (``Ego`` -> ``Jaz`` ->
    ``Enotnost``) as well as a current ``tension`` and ``emotion`` level.
    State transitions occur when either ``tension`` exceeds ``0.7`` or
    ``emotion`` exceeds ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = "neutral"
        self.history = [state]

    def feel(self, label: str, intensity: float) -> None:
        """Set the current emotion and adjust tension.

        Parameters
        ----------
        label:
            Name of the emotion (e.g. ``"fear"`` or ``"joy"``).
        intensity:
            Strength of the emotion on a ``0-1`` scale.  Emotion directly
            influences ``tension``.
        """

        self.emotion_label = label
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

    def principle(self) -> str:
        """Return the philosophical principle for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.principle()
        return f"({self.emotion_label}) {base}"

    def speak(self, question: str) -> str:
        """Speak an answer and possibly change state based on emotion."""
        reply = self.respond(question)
        self.transition()
        return f"{self.name} ({self.state}): {reply}"

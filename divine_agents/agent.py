class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent holds information about its ontological ``state`` (``Ego``, ``Jaz``
    or ``Enotnost``) alongside the current ``tension`` level and emotional
    information.  Emotions are represented with a ``type`` (e.g. ``fear``,
    ``joy``) and ``intensity`` in the range ``0``-``1``.  Transitions between
    states occur when either the tension or the emotional intensity exceed the
    configured thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_type: str = "neutral",
        emotion_intensity: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_type = emotion_type
        self.emotion_intensity = emotion_intensity
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion and adjust tension.

        Parameters
        ----------
        emotion_type:
            Type of the emotion (e.g. ``fear``, ``joy``).
        intensity:
            Intensity in the range ``0``-``1``.  The value also contributes to
            the agent's ``tension`` level.
        """
        self.emotion_type = emotion_type
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
        prefix = self.emotion_type.capitalize() if self.emotion_type != "neutral" else ""
        if self.state == "Ego":
            view = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            view = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            view = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}: {view}" if prefix else view

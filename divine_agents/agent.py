class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent keeps track of its current ontological ``state`` and emotional
    ``tension``.  Transitions between states occur only when the internal
    ``tension`` exceeds ``0.7`` or the ``emotion`` intensity is greater than
    ``0.5``.  Emotion is represented with a numeric intensity and a textual
    description such as ``fear`` or ``joy``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and increase tension accordingly."""
        self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        The answer is coloured with the agent's current emotional tone.
        """
        emotion_prefix = {
            "fear": "S tresočim glasom",
            "anger": "Z jeznim tonom",
            "joy": "Z veseljem",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}".strip()

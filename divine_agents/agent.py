class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent holds an ontological ``state`` (``Ego``, ``Jaz`` or
    ``Enotnost``) together with an ``emotion`` intensity and label.  The
    combination of ``emotion`` and ``tension`` determines when a state
    transition should occur.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity in the range ``0..1``.
        label:
            Human readable description of the emotion (e.g. ``"fear"`` or
            ``"joy"``).  This label influences how the agent responds in a
            dialogue.
        """
        self.emotion = value
        self.emotion_label = label
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
        """Return a philosophical answer depending on the current and emotional state."""
        emotion_prefix = {
            "fear": "S strahom povem, da ",
            "joy": "Z veseljem povem, da ",
            "anger": "Z jezo trdim, da ",
        }.get(self.emotion_label, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{emotion_prefix}{base}"

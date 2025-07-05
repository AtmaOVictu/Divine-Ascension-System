class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent keeps track of its ontological ``state`` together with its current
    emotional intensity and type.  The :py:meth:`transition` method is triggered
    when either the ``tension`` exceeds ``0.7`` or ``emotion`` exceeds
    ``0.5`` as required by the specification.
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

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in the ``0.0`` - ``1.0`` range.
        kind:
            Human readable name of the emotion (e.g. ``"fear"``, ``"joy"``).
        """
        self.emotion = value
        self.emotion_type = kind
        # Any emotion contributes to the overall tension of the agent.
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
        """Return a philosophical answer influenced by emotion and state."""

        prefixes = {
            "fear": "S strahom povem, ",
            "joy": "Z veseljem povem, ",
            "anger": "Z jezo izjavljam, ",
            "neutral": "",
        }

        prefix = prefixes.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}"

"""Core classes representing ontological agents."""

class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``Ego`` | ``Jaz`` | ``Enotnost``).
    tension:
        Current tension level in the range ``0.0``-``1.0``.
    emotion:
        Intensity of the agent's emotion.
    emotion_type:
        Descriptive label for the emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and type.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_type:
            Optional name of the emotion. If provided, the agent's emotion type
            will be updated as well.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # emotional intensity feeds back into tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if tension or emotion exceed thresholds."""
        if (self.tension > 0.7 or self.emotion > 0.5) and self.state != "Enotnost":
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.PRINCIPLES.get(self.state, "")
        if self.emotion_type != "neutral":
            prefix = f"({self.emotion_type}) "
        else:
            prefix = ""
        return prefix + base

    def introspect(self) -> str:
        """Return a textual representation of the agent's state history."""
        return f"{self.name} states: {' -> '.join(self.history)}"

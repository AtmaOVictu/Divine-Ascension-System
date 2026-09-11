class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The agent's identifier.
    state:
        Starting ontological state. Defaults to ``"Ego"``.
    tension:
        Initial tension level in the ``[0, 1]`` interval.
    emotion:
        Initial emotion intensity in the ``[0, 1]`` interval.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = "neutral"
        self.history = [state]
        # Each frame stores a snapshot of the agent's state, emotion and tension
        self.frames = [{"state": state, "emotion": emotion, "tension": tension}]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity and label while adjusting tension.

        Parameters
        ----------
        value:
            Intensity of the emotion in ``[0, 1]``.
        label:
            Descriptive name of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.emotion = max(0.0, min(1.0, value))
        self.emotion_label = label
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamped to ``[0, 1]``."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and log a frame."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        self.history.append(self.state)
        self.frames.append(
            {
                "state": self.state,
                "emotion": self.emotion,
                "emotion_label": self.emotion_label,
                "tension": self.tension,
            }
        )
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def get_history(self) -> list:
        """Return the chronological list of states."""
        return self.history

    def get_frames(self) -> list:
        """Return the detailed frame history."""
        return self.frames

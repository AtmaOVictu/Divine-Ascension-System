class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "nevtralno"):
        """Initialize a new agent.

        Parameters
        ----------
        name: str
            Identifier of the agent.
        state: str, optional
            Starting ontological state, defaults to ``"Ego"``.
        tension: float, optional
            Base tension level influencing state transitions.
        emotion: float, optional
            Current emotion intensity.
        emotion_type: str, optional
            Type of emotion (npr. "strah", "veselje", ...).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and type and adjust tension.

        Parameters
        ----------
        value: float
            Intensity of the emotion.
        emotion_type: str
            Type of emotion (``"strah"``, ``"veselje"``, ``"jeza"`` ...).
        """
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def response_with_emotion(self, message: str) -> str:
        """Prepend an emotional prefix to ``message`` based on ``emotion_type``."""
        prefixes = {
            "strah": "S strahom",
            "veselje": "Z veseljem",
            "jeza": "S jezo",
        }
        prefix = prefixes.get(self.emotion_type, "S nevtralnostjo")
        return f"{prefix}: {message}"

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer prefixed with emotional context."""
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."
        return self.response_with_emotion(msg)

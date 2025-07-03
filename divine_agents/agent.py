class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        *,
        tension_threshold: float = 0.7,
        emotion_threshold: float = 0.5,
    ):
        """Initialize a new agent.

        Parameters
        ----------
        name: str
            Display name of the agent.
        state: str, default "Ego"
            Initial ontological state.
        tension: float, default 0.0
            Starting tension value.
        emotion: float, default 0.0
            Starting emotion intensity.
        tension_threshold: float, default 0.7
            Tension value required for a state transition.
        emotion_threshold: float, default 0.5
            Emotion value required for a state transition.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.tension > self.tension_threshold
            or self.emotion > self.emotion_threshold
        ):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

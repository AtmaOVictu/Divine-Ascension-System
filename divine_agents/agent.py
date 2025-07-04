class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None) -> None:
        """Create an agent with a given ontological state.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Initial ontological state. Defaults to ``"Ego"``.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_name:
            Label describing the current emotion (e.g. ``"fear"``).
        """

        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update the emotion intensity and optionally set an emotion name."""

        self.emotion = value
        if emotion_name:
            self.emotion_name = emotion_name
        # Emotion increases overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when tension or emotion exceed thresholds."""

        if self.tension > 0.7 or self.emotion > 0.5:
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

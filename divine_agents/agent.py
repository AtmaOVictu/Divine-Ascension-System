class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier of the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_name:
            Optional label for the current emotion (e.g. "strah", "jeza").
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_name:
            Optional descriptive label for the emotion.
        """

        self.emotion = value
        self.tension += value
        if emotion_name:
            self.emotion_name = emotion_name

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
        """Return a philosophical answer influenced by the current state and emotion."""

        prefix = ""
        if self.emotion_name != "neutral":
            prefix = f"Čutim {self.emotion_name}. "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return prefix + base

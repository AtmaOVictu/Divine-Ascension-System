class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "nevtralno"):
        """Create a new agent.

        Parameters
        ----------
        name: str
            Name of the agent.
        state: str, optional
            Initial ontological state.
        tension: float, optional
            Initial tension level.
        emotion: float, optional
            Initial emotion intensity.
        emotion_name: str, optional
            Descriptive name of the current emotion.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion.
        name:
            Optional descriptive name of the emotion (e.g. ``"strah"``).
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
        # Emotions contribute to overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            principle = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            principle = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            principle = "Vse resnice so eno, medsebojno povezane."

        return f"({self.emotion_name}) {principle}"

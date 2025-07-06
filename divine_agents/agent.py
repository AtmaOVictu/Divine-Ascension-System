class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state of the agent (Ego, Jaz, Enotnost).
    tension: float
        Accumulated tension level influencing transitions.
    emotion: float
        Current emotion intensity.
    emotion_name: str
        Label of the current dominant emotion (e.g., 'jeza', 'strah').
    history: list[str]
        Collection of states the agent has been in.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            Intensity of the emotion in range [0, 1].
        name: str
            Descriptive label of the emotion (e.g., 'strah', 'jeza').
        """
        self.emotion = value
        self.emotion_name = name
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name != "neutral":
            base = f"{base} (Čustvo: {self.emotion_name})"
        return base

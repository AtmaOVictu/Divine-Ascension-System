class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks a hidden emotion label that is not revealed in responses
    unless explicitly requested. This label stores the current emotion type and
    intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]
        # emotion label is hidden metadata
        self.emotion_label = {"type": emotion_type, "value": emotion}

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity.
        emotion_type: str | None
            Optional label of the emotion (e.g. 'strah', 'veselje').
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value
        self.emotion_label = {"type": self.emotion_type, "value": self.emotion}

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def get_emotion_label(self) -> dict:
        """Return the current hidden emotion label."""
        return self.emotion_label

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str, reveal_emotion: bool = False) -> str:
        """Return a philosophical answer depending on the current state.

        Parameters
        ----------
        question: str
            Question posed to the agent. (Currently unused but kept for
            extensibility.)
        reveal_emotion: bool, optional
            If ``True``, include the hidden emotion label in the response.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if reveal_emotion and self.emotion_type != "neutral":
            base += f" Čustvo: {self.emotion_type}."
        return base

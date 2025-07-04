class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        The name of the agent.
    state : str
        Current ontological state (Ego, Jaz or Enotnost).
    tension : float
        Accumulated tension level.
    emotion : float
        Current emotional intensity.
    emotion_kind : str
        Label for the prevailing emotion (e.g. 'fear', 'joy').
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_kind: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_kind = emotion_kind
        self.history = [state]

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            New emotional intensity.
        kind : str, optional
            Label describing the emotion type, by default "neutral".
        """
        self.emotion = value
        self.emotion_kind = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def describe_emotion(self) -> str:
        """Return a short textual description of the agent's emotion."""
        return f"{self.emotion_kind} ({self.emotion:.2f})"

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
        """Return a philosophical answer depending on the current state."""
        prefix = f"[{self.describe_emotion()}]"
        if self.state == "Ego":
            return prefix + " Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + " Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + " Vse resnice so eno, medsebojno povezane."

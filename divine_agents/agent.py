class Agent:
    """Ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state (Ego, Jaz, or Enotnost).
    tension: float
        Accumulated tension influencing state transitions.
    emotion: float
        Intensity of the current emotion in the range ``0.0`` - ``1.0``.
    emotion_type: str
        Type of emotion (e.g. ``fear``, ``joy``, ``anger``).
    history: List[str]
        History of states the agent has been through.
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

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in the range ``0.0`` - ``1.0``.
        emotion_type:
            Type of the emotion which may colour the agent's responses.
        """
        self.emotion = value
        self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        The tone of the response is lightly influenced by the current
        ``emotion_type``.
        """
        emotion_part = ""
        if self.emotion_type != "neutral":
            emotion_part = f" ({self.emotion_type})"

        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_part}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_part}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_part}"

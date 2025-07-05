class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Identifier for the agent.
    state : str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension : float
        Numerical measure of the agent's inner tension.
    emotion_level : float
        Intensity of the current emotion in the range ``0-1``.
    emotion_type : str
        Label describing the current emotion (e.g. ``joy`` or ``fear``).
    history : list[str]
        History of states the agent has transitioned through.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, level: float, emotion_type: str = "neutral") -> None:
        """Update emotional state and adjust tension.

        Parameters
        ----------
        level : float
            New emotional intensity between ``0`` and ``1``.
        emotion_type : str, optional
            Descriptive label for the emotion.
        """

        self.emotion_level = level
        self.emotion_type = emotion_type
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = ""
        if self.emotion_type and self.emotion_type != "neutral":
            prefix = f"({self.emotion_type}) "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return prefix + base

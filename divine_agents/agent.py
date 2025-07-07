class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
        """Initialize a new :class:`Agent`.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_name:
            Name of the current predominant emotion.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update the emotional state and intensity.

        The new emotion value also increases the current tension.
        """
        self.emotion_name = emotion
        self.emotion = value
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
        """Return a philosophical answer influenced by emotion and state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name == "fear":
            return f"{base} Občutim strah, ki krepi mojo napetost."
        if self.emotion_name == "joy":
            return f"{base} Občutim veselje, ki me odpira novim pogledom."
        if self.emotion_name == "anger":
            return f"{base} Jeza me sili v iskanje spremembe."
        return base

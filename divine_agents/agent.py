class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Base tension value. High tension may trigger a state change.
    emotion:
        Intensity of the current emotion. Values over ``0.5`` may
        also trigger a state change.
    emotion_type:
        Qualitative label of the current emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and label and adjust tension accordingly."""
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.emotion_type == "fear":
            prefix = "S strahom povem: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem povem: "
        elif self.emotion_type == "anger":
            prefix = "Z jezo trdim: "
        elif self.emotion_type == "sorrow":
            prefix = "Žalosten pravim: "
        else:
            prefix = ""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base

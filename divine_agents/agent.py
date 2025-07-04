class Agent:
    """Ontological agent that transitions between philosophical states.

    The agent can move from ``Ego`` to ``Jaz`` and finally ``Enotnost``. The
    change is triggered when either the internal ``tension`` exceeds ``0.7`` or
    the current ``emotion`` intensity is above ``0.5``.  Emotions influence the
    responses the agent gives during a dialogue.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set emotion type with a given intensity."""
        self.emotion_type = kind
        self.update_emotion(intensity)

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
        prefix = ""
        if self.emotion_type == "anger":
            prefix = "Z jezo trdim, da "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem menim, da "
        elif self.emotion_type == "fear":
            prefix = "S strahom predlagam, da "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core

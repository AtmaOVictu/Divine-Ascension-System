class Agent:
    """Ontological agent capable of emotional state driven transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    #: how much a given emotion influences tension
    EMOTION_TENSION_EFFECT = {
        "neutral": 0.0,
        "fear": 1.0,
        "joy": -0.5,
        "anger": 1.0,
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_state: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion_state(self, state: str, intensity: float) -> None:
        """Set emotional state and modify tension based on intensity."""
        if state not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion state: {state}")
        self.emotion_state = state
        effect = self.EMOTION_TENSION_EFFECT.get(state, 0.0)
        self.update_emotion(intensity)
        self.tension += intensity * effect
        # ensure tension stays within [0, 1.0]
        self.tension = max(0.0, min(self.tension, 1.0))

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
        """Return a philosophical answer depending on state and emotion."""
        prefix = {
            "fear": "Zaskrbljeno pravi: ",
            "joy": "Veselo pravi: ",
            "anger": "Jezno pravi: ",
            "neutral": "",
        }.get(self.emotion_state, "")

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core

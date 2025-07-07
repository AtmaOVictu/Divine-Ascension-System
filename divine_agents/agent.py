class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update unnamed emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def experience_emotion(self, emotion_type: str, intensity: float) -> None:
        """Experience a named emotion which influences tension."""
        if emotion_type not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion type: {emotion_type}")
        self.emotion_type = emotion_type
        self.emotion = intensity

        if emotion_type in ("fear", "anger"):
            self.tension += intensity
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - intensity / 2)
        else:
            self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if tension or emotion exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        prefix = {
            "fear": "S strahom razmišljam, ",
            "joy": "Z veseljem pravim, ",
            "anger": "Z jezo trdim, ",
            "neutral": "",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core

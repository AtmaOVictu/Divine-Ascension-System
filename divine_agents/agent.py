class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: str = "neutral", emotion_level: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_level = emotion_level
        self.history = [state]

    def set_emotion(self, emotion: str, intensity: float) -> None:
        """Update the agent's emotion label and intensity and adjust tension."""
        if emotion not in self.EMOTIONS:
            raise ValueError(f"Unsupported emotion: {emotion}")
        self.emotion = emotion
        self.emotion_level = intensity
        if intensity > 0:
            self.tension += intensity

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
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion == "fear":
            prefix = "V strahu povem, da "
        elif self.emotion == "joy":
            prefix = "Z veseljem povem, da "
        elif self.emotion == "anger":
            prefix = "Jezen izjavljam, da "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base

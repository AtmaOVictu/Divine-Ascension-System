class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of emotional labels to intensity values
    EMOTIONS = {
        "fear": 0.4,
        "joy": 0.7,
        "anger": 0.6,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = emotion
        self.history = [state]

    def emotion_intensity(self) -> float:
        """Return the numeric intensity of the current emotion."""
        return self.EMOTIONS.get(self.emotion, 0.0)

    def update_emotion(self, emotion: str) -> None:
        """Update emotion label and adjust tension based on its intensity."""
        self.emotion = emotion
        self.tension += self.emotion_intensity()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if tension or emotion thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion == "joy":
            prefix = "With joy: "
        elif self.emotion == "fear":
            prefix = "With fear: "
        elif self.emotion == "anger":
            prefix = "With anger: "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

import uuid

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_EFFECTS = {
        "fear": 1.0,
        "anger": 1.0,
        "joy": -0.5,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.id = uuid.uuid4()
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension based on the emotion type."""
        self.emotion = value
        self.emotion_type = emotion_type
        factor = self.EMOTION_EFFECTS.get(emotion_type, 0.0)
        self.tension = max(0.0, self.tension + value * factor)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
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
        """Return a philosophical answer depending on current state and emotion."""
        emotion_prefix = ""
        if self.emotion_type == "fear":
            emotion_prefix = "V strahu trdim, da "
        elif self.emotion_type == "anger":
            emotion_prefix = "Z jezo menim, da "
        elif self.emotion_type == "joy":
            emotion_prefix = "Z veseljem verjamem, da "

        if self.state == "Ego":
            return f"{emotion_prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotion_prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{emotion_prefix}Vse resnice so eno, medsebojno povezane."

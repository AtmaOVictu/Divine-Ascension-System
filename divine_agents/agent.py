class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Set emotion type and intensity, adjusting tension accordingly."""
        delta = value - self.emotion
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += delta

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
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_phrase = ""
        if self.emotion_type == "fear":
            emotion_phrase = " Čutim strah, zato to zagovarjam."
        elif self.emotion_type == "joy":
            emotion_phrase = " Z veseljem delim to misel."
        elif self.emotion_type == "anger":
            emotion_phrase = " Jeza me vodi v ta odgovor."

        return base + emotion_phrase

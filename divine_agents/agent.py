class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }
    EMOTION_WORDS = {"fear": "strah", "joy": "veselje", "anger": "jezo"}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on state and emotion."""
        base = self.PRINCIPLES.get(self.state, "")
        emotion_note = ""
        if self.emotion_type != "neutral":
            sl_word = self.EMOTION_WORDS.get(self.emotion_type, self.emotion_type)
            emotion_note = f" Čutim {sl_word}."
        return base + emotion_note

class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_EFFECT = {
        "fear": 1.0,
        "anger": 1.0,
        "joy": -0.5,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = value
        effect = self.EMOTION_EFFECT.get(emotion_type, 0.0)
        self.tension = max(0.0, self.tension + value * effect)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, value)

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_suffix = {
            "fear": " Moja čustva so prežeta s strahom.",
            "anger": " Občutim jezo v tem razmišljanju.",
            "joy": " To me navdaja z veseljem.",
        }.get(self.emotion_type, "")

        return f"{base}{emotion_suffix}"

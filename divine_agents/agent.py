class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    EMOTION_MODIFIERS = {
        "joy": " Čutim radost.",
        "fear": " Prežema me strah.",
        "anger": " Jeza me drži budnega.",
        "neutral": "",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def set_emotion(self, value: float, name: str) -> None:
        """Set emotion value and name, adjusting tension."""
        self.emotion = value
        self.emotion_name = name
        self.tension += value

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity without changing emotion name."""
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
        """Return a philosophical answer depending on current state and emotion."""
        base = self.PHILOSOPHY.get(self.state, "")
        emotion = self.EMOTION_MODIFIERS.get(self.emotion_name, "")
        return f"{base}{emotion}"

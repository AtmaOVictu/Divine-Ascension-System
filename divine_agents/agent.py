class Agent:
    """Ontological agent with emotion-driven state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_EFFECTS = {
        "fear": 0.3,
        "anger": 0.4,
        "joy": -0.2,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set the emotional state and modify tension."""
        self.emotion_label = label
        self.emotion = intensity
        self.tension += intensity + self.EMOTION_EFFECTS.get(label, 0)

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
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_prefix = {
            "fear": "V strahu, ",
            "anger": "V jezi, ",
            "joy": "V veselju, ",
            "neutral": "",
        }.get(self.emotion_label, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix}{base}"

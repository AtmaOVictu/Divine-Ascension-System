class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: influence of emotions on tension
    EMOTION_EFFECTS = {
        "fear": 0.4,
        "anger": 0.5,
        "joy": -0.2,
        "sorrow": 0.3,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state
        self.history = [state]

    def experience_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion by name and adjust tension accordingly."""
        self.emotion_state = name
        self.emotion = intensity
        self.tension += intensity + self.EMOTION_EFFECTS.get(name, 0.0)

    def update_emotion(self, value: float) -> None:
        """Backward-compatible method to directly set emotion intensity."""
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
        """Return a philosophical answer depending on ontological and emotional state."""
        prefix = f"[{self.emotion_state}] " if self.emotion_state != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

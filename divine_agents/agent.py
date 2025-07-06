"""Core agent model used throughout the philosophical simulations."""

class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def perceive_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the agent's emotion and adjust tension."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

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
        base = self.PRINCIPLES[self.state]
        if self.emotion_type == "anger":
            return f"{base} Čutim jezo!"
        if self.emotion_type == "fear":
            return f"{base} Strah me je."
        if self.emotion_type == "joy":
            return f"{base} Vesel sem."
        return base

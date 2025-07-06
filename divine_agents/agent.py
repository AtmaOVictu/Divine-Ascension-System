class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = "neutral"
        self.history = [state]

    def set_emotion(self, name: str, value: float) -> None:
        """Set emotion type and intensity, adjusting tension."""
        self.emotion_name = name
        self.emotion = value
        self.tension += value

    def update_emotion(self, value: float) -> None:
        """Backward compatible method to update unnamed emotion."""
        self.set_emotion("neutral", value)

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name == "fear":
            return f"{base} Čutim strah."
        if self.emotion_name == "anger":
            return f"{base} Čutim jezo."
        if self.emotion_name == "joy":
            return f"{base} Čutim radost."
        return base

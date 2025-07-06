class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state
        self.history = [state]

    def update_emotion(self, value: float, emotion_state: str = "neutral") -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        if emotion_state in self.EMOTIONS:
            self.emotion_state = emotion_state
        if self.emotion_state == "fear":
            self.tension += value + 0.2
        elif self.emotion_state == "anger":
            self.tension += value + 0.3
        elif self.emotion_state == "joy":
            self.tension += max(0.0, value - 0.2)
        else:
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
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_tag = {
            "fear": " Čutim strah, kar povečuje mojo napetost.",
            "joy": " Čutim veselje, kar me pomirja.",
            "anger": " Čutim jezo, kar me vznemirja.",
        }.get(self.emotion_state, "")

        return base + emotion_tag

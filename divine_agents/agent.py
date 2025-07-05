class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and type and adjust tension."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and emotions are considered."""
        if self.emotion_type == "fear" and self.tension > 0.8:
            self.state = "Ego"
        elif self.emotion_type == "joy" and self.tension < 0.3:
            self.state = "Jaz"
        elif self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base_response = ""
        if self.state == "Ego":
            base_response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base_response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base_response = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "anger":
            return f"{base_response} Toda, jaz sem jezen in to spreminja moje dojemanje resnice."
        if self.emotion_type == "joy":
            return f"{base_response} Veselje me vodi k širšim obzorjem resnice."
        if self.emotion_type == "fear":
            return f"{base_response} Strah me ovira pri sprejemanju polne resnice."

        return base_response

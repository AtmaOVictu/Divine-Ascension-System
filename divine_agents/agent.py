class Agent:
    """Represent an ontological agent with emotions and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", emotion: float = 0.0,
                 emotion_type: str = "nevtralno", tension: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.tension = tension
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity, type and adjust tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def response_with_emotion(self, message: str) -> str:
        """Return message prefixed with the current emotional state."""
        if self.emotion_type == "strah":
            return f"S strahom: {message}"
        if self.emotion_type == "veselje":
            return f"Z veseljem: {message}"
        if self.emotion_type == "jeza":
            return f"S jezo: {message}"
        return f"S nevtralnostjo: {message}"

    def respond(self, question: str) -> str:
        """Return a philosophical statement based on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return self.response_with_emotion(answer)

    def __str__(self) -> str:
        return (
            f"Agent {self.name} je v stanju {self.state}, "
            f"čustvo: {self.emotion_type}, zgodovina: {self.history}"
        )

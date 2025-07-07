class Agent:
    """Ontological agent capable of state transitions influenced by emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = {
        "fear": 0.3,
        "joy": 0.7,
        "anger": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", emotion: str = "joy", tension: float = 0.0):
        self.name = name
        self.state = state
        self.emotion = emotion
        self.tension = tension
        self.history = [state]

    def update_emotion(self, emotion: str) -> None:
        """Update emotional label and adjust tension using predefined intensity."""
        self.emotion = emotion
        self.tension += self.EMOTIONS.get(emotion, 0.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states when emotion or tension exceed thresholds."""
        emotion_value = self.EMOTIONS.get(self.emotion, 0.0)
        if self.tension > 0.7 or emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Generate a philosophical response considering state and emotion."""
        prefix = {
            "joy": "With joy: ",
            "fear": "With fear: ",
            "anger": "With anger: ",
        }.get(self.emotion, "")

        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{msg}"

class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def apply_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Apply an emotion and increase tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    # Backwards compatible method name
    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        self.apply_emotion(value, emotion_type)

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
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            base += " Občutim strah, kar povečuje mojo napetost."
        elif self.emotion_type == "joy":
            base += " Preveva me veselje, kar me umirja."
        elif self.emotion_type == "anger":
            base += " Jeza me vodi k spremembi stališča."
        return base

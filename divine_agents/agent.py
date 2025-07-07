class Agent:
    """Ontological agent capable of state transitions based on tension and emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        if emotion_type in {"fear", "anger"}:
            self.tension += intensity
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - intensity * 0.5)
        else:
            self.tension += intensity * 0.2

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_suffix = {
            "fear": " Občutim strah.",
            "joy": " Občutim veselje.",
            "anger": " Občutim jezo."
        }.get(self.emotion_type, "")

        return f"{base}{emotion_suffix}"

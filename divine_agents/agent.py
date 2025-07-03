class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_name: str | None = None,
        emotion_level: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_name = emotion_name or "neutral"
        self.emotion_level = emotion_level
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Set emotion and adjust tension accordingly."""
        self.emotion_name = name
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly update tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an answer reflecting the agent's state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion_name})"

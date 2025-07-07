class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = emotions or {}
        self.current_emotion: str | None = None
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update an emotion and adjust tension accordingly."""
        self.emotions[name] = value
        self.current_emotion = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_threshold = any(v > 0.5 for v in self.emotions.values())
        if self.tension > 0.7 or emotion_threshold:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_phrase = f" Čutim {self.current_emotion}." if self.current_emotion else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_phrase
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_phrase
        return "Vse resnice so eno, medsebojno povezane." + emotion_phrase

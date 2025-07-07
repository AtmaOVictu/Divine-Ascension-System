class Agent:
    """Ontological agent capable of state transitions and emotional responses."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and adjust tension."""
        self.emotions[name] = value
        self.tension += value

    def dominant_emotion(self) -> tuple:
        """Return the emotion with the highest intensity."""
        if not self.emotions:
            return ("neutral", 0.0)
        return max(self.emotions.items(), key=lambda item: item[1])

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        _, intensity = self.dominant_emotion()
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        emotion, intensity = self.dominant_emotion()
        mood = f" (emotion: {emotion})" if intensity > 0.5 else ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base}{mood}"

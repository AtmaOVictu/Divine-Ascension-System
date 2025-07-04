class Agent:
    """Ontological agent capable of emotional transitions and dialogue."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, mood: str = "calm"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, value: float, mood: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if mood is not None:
            self.mood = mood

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
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def dialogue_line(self, question: str) -> str:
        """Compose a dialogue line including mood and state."""
        response = self.respond(question)
        return f"{self.name} ({self.state}, {self.mood}): {response}"

    def transition_line(self) -> str:
        """Perform transition and return a descriptive line."""
        previous = self.state
        new_state = self.transition()
        if new_state != previous:
            return f"{self.name} prehaja v stanje: {new_state}"
        return f"{self.name} ostaja v stanju: {new_state}"

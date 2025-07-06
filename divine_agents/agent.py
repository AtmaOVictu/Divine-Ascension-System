class Agent:
    """Ontological agent capable of state transitions based on tension and emotions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        if state not in self.STATES:
            raise ValueError(f"Invalid state: {state}")
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion_level = 0.0
        self.emotion: str | None = None
        self.history = [state]

    def update_tension(self, value: float) -> None:
        """Increase tension by ``value``."""
        self.tension += value

    def feel(self, emotion: str, intensity: float) -> None:
        """Set the current emotion and adjust tension accordingly."""
        self.emotion = emotion
        self.emotion_level = intensity
        self.update_tension(intensity)
        self.transition()

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."

        if self.emotion:
            response += f" (občuti {self.emotion})"
        return response

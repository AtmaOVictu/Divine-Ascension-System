class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class AgentInstance(Agent):
    """Specific instance of an agent with an additional weekly level."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, weekly_level: int = 0):
        super().__init__(name, state, tension, emotion)
        self.weekly_level = weekly_level

    def transition(self) -> str:
        """Transition and annotate the state with the weekly level."""
        super().transition()
        if not self.state.startswith("tedenski nivo"):
            self.state = f"tedenski nivo {self.weekly_level}" if self.state != "Ego" else self.state
        self.history[-1] = self.state
        return self.state

    def respond(self, question: str) -> str:
        base = super().respond(question)
        return f"Instanca {self.name} odgovarja z nivojem {self.weekly_level}. {base}"

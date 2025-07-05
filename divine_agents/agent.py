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


class SecondaryAgent(Agent):
    """Agent that monitors another agent and can intervene."""

    def __init__(self, name: str, main_agent: Agent):
        super().__init__(name)
        self.main_agent = main_agent

    def monitor_main_agent(self) -> None:
        """Intervene when the main agent reaches ENOTNOST with low tension."""
        if (
            self.main_agent.state == "Enotnost"
            and self.main_agent.tension < 0.5
        ):
            self.state = "Jaz"
            # trigger emotional reaction
            self.update_emotion(0.5)

    def respond(self, question: str) -> str:  # type: ignore[override]
        """Respond based on own state when acting as monitor."""
        if self.state == "Ego":
            return f"{self.name}: I am here to observe."
        if self.state == "Jaz":
            return f"{self.name}: I offer alternative perspectives."
        return f"{self.name}: I am a silent observer of interconnected truths."

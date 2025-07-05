class LoadingScreenUnity:
    """Simple loading progress toward Unity."""

    def __init__(self, agent_name: str, max_value: int = 3):
        self.agent_name = agent_name
        self.unity_value = 0
        self.max_value = max_value

    def transition(self) -> int:
        """Increase progress toward Unity until max_value."""
        if self.unity_value < self.max_value:
            self.unity_value += 1
        return self.unity_value


class PhilosopherAgent(LoadingScreenUnity):
    """Agent that can transition through philosophical states and Unity."""

    STATES = ("Ego", "Jaz", "Enotnost", "Enlightened")

    def __init__(self, name: str, state: str = "Ego", max_value: int = 3):
        super().__init__(name, max_value)
        self.state = state
        self.tension = 0.0
        self.emotion = 0.0
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def state_transition(self) -> str:
        """Transition between philosophical states based on thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical statement depending on state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return "Agent je razsvetljen v enotni resnici."

    def transition(self) -> str:  # type: ignore[override]
        """Perform Unity transition and possibly reach enlightenment."""
        super().transition()
        if self.unity_value == self.max_value:
            self.state = "Enlightened"
        return self.state

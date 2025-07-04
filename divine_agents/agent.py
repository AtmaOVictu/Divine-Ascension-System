class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        ego_ratio: float = 0.49,
        jaz_ratio: float = 0.51,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.ego_ratio = ego_ratio
        self.jaz_ratio = jaz_ratio
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
                self.ego_ratio = max(0.0, self.ego_ratio - 0.05)
                self.jaz_ratio = min(1.0, self.jaz_ratio + 0.05)
            elif self.state == "Jaz":
                self.state = "Enotnost"
                self.jaz_ratio = max(0.0, self.jaz_ratio - 0.05)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        ratio_info = f"(ego_ratio={self.ego_ratio:.2f}, jaz_ratio={self.jaz_ratio:.2f})"
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih. {ratio_info}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi. {ratio_info}"
        return f"Vse resnice so eno, medsebojno povezane. {ratio_info}"

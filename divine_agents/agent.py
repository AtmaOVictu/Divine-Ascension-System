class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        temperature: float = 20.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.temperature = temperature
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def color(self) -> tuple:
        """Return RGB color representing current temperature."""
        if self.temperature < 0:
            return (0, 0, 1)
        if self.temperature < 25:
            return (0, 0.5, 0)
        if self.temperature < 50:
            return (1, 1, 0)
        return (1, 0, 0)

    def update_temperature(self, value: float) -> None:
        """Set temperature and adjust emotion based on change."""
        self.temperature = value
        # Higher temperature increases emotion slightly
        self.emotion = min(1.0, max(0.0, self.emotion + value / 100))

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
            base = "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return f"{base} Čutim to zelo močno!"
        if self.emotion < 0.3:
            return f"{base} O tem sem precej miren."
        return base

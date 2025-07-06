class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.opposite = None

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def define_opposite(self, opposite: "OppositeAgent") -> None:
        """Assign an opposite agent representing a contrary concept."""
        self.opposite = opposite

    def debate(self) -> list[str]:
        """Debate with the assigned opposite and trigger state transition."""
        if not self.opposite:
            return []
        lines = [
            f"{self.name} in {self.opposite.name} ustvarjata dialekti\u010dno napetost."
        ]
        # Activation of opposite increases emotion and tension
        self.update_emotion(0.6)
        lines.append(f"{self.name} prehaja v stanje: {self.transition()}")
        lines.append(f"{self.name}: {self.respond('Kaj je resnica?')}")
        return lines

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

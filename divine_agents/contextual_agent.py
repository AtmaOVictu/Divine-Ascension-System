class ContextualAgent:
    """Agent with internal and external context for state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str):
        self.name = name
        self.state = "Ego"
        self.tension = 0.0
        self.emotion = 0.0
        self.internal_context = None
        self.external_context = None
        self.history = [self.state]

    def set_context(self, internal: str, external: str) -> None:
        """Set internal and external context for the agent."""
        self.internal_context = internal
        self.external_context = external

    def update_emotion(self, value: float) -> None:
        """Update emotion and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly update tension."""
        self.tension = value

    def _transition_to_jaz(self) -> None:
        self.state = "Jaz"

    def _transition_to_enotnost(self) -> None:
        self.state = "Enotnost"

    def transition(self) -> str:
        """Transition based on tension and emotion thresholds."""
        if self.state == "Ego" and (self.tension > 0.7 or self.emotion > 0.5):
            self._transition_to_jaz()
        elif self.state == "Jaz" and (self.tension > 0.7 or self.emotion > 0.5):
            self._transition_to_enotnost()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Respond according to current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z nasimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def contextual_transition(self) -> str:
        """Transition using internal and external context."""
        if self.internal_context == "visoka napetost" and self.external_context == "stresno okolje":
            self.update_tension(0.8)
        if self.internal_context == "mirno" and self.external_context == "podpora":
            self.update_tension(1.0)
        return self.transition()

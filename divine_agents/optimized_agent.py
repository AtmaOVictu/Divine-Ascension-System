class OptimizedAgent:
    """Represents an ontological agent with optimized transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, pathos: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension and pathos, then optimize."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for transition."""
        self.tension = value
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        """Optimize transition logic based on tension, emotion, and pathos."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> None:
        """Perform state transition following ontological order."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base_response = self._generate_response_base()
        emotional_response = self._generate_emotional_feedback()
        return f"{base_response} {emotional_response}"

    def _generate_response_base(self) -> str:
        """Generate philosophical response based on current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def _generate_emotional_feedback(self) -> str:
        """Return emotional statement based on emotion level."""
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

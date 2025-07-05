class OptimizedAgent:
    """Represents an ontological agent with optimized transitions."""

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
        """Update emotion intensity, adjust tension and pathos, then transition."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        """Trigger a transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> None:
        """Move the agent to the next ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)

    def respond(self, question: str) -> str:
        """Return a response influenced by state and emotion."""
        base = self.generate_response_base()
        emotional = self.generate_emotional_feedback()
        return f"{base} {emotional}"

    def generate_response_base(self) -> str:
        """Generate the philosophical base of the response."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def generate_emotional_feedback(self) -> str:
        """Add emotional context to the response."""
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

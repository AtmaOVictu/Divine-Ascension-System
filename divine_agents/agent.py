class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, pathos: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

    # --------------------------- update methods ---------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension and pathos."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and evaluate transitions."""
        self.tension = value
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    # --------------------------- transition logic ---------------------------
    def optimize_transition(self) -> None:
        """Optimize transition logic based on emotion and tension thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.transition()

    def transition(self) -> str:
        """Perform a state transition following the ontological order."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # --------------------------- responses ---------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self.generate_response_base()
        feedback = self.generate_emotional_feedback()
        return f"{base} {feedback}".strip()

    def generate_response_base(self) -> str:
        """Generate base philosophical response based on current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def generate_emotional_feedback(self) -> str:
        """Provide emotional feedback based on current emotion level."""
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

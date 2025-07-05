class Agent:
    """Ontological agent capable of transitioning states based on emotions and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        pathos: float = 0.0,
        birth_params: dict | None = None,
        parent_params: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

        self.birth_params = birth_params or {}
        self.parent_params = parent_params or {}

        self.apply_birth_params()
        self.apply_parental_influence()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension and pathos, and optimise transitions."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for transition."""
        self.tension = value
        self.optimize_transition()

    def apply_birth_params(self) -> None:
        """Initialise tension and emotion from birth parameters."""
        self.tension += self.birth_params.get("initial_tension", 0.0)
        self.emotion += self.birth_params.get("initial_emotion", 0.0)

    def apply_parental_influence(self) -> None:
        """Adjust agent's parameters based on parental influence."""
        self.tension += self.parent_params.get("parental_tension", 0.0)
        self.emotion += self.parent_params.get("parental_emotion", 0.0)
        self.pathos += self.parent_params.get("parental_pathos", 0.0)

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        """Optimise transition logic based on tension, emotion and pathos."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        base_response = self.generate_response_base()
        emotional_response = self.generate_emotional_feedback()
        return f"{base_response} {emotional_response}"

    # Helper methods
    def generate_response_base(self) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def generate_emotional_feedback(self) -> str:
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

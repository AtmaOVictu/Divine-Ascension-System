class Agent:
    """Represents an ontological agent with dynamic state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, birth_params: dict | None = None,
                 parent_params: dict | None = None,
                 state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, pathos: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

        self.birth_params = birth_params or {}
        self.parent_params = parent_params or {}

        self._apply_birth_params()
        self._apply_parental_influence()

    # ------------------------------------------------------------------
    # Initialization helpers
    # ------------------------------------------------------------------
    def _apply_birth_params(self) -> None:
        """Initialize tension and emotion from birth parameters."""
        self.tension += self.birth_params.get("initial_tension", 0)
        self.emotion += self.birth_params.get("initial_emotion", 0)

    def _apply_parental_influence(self) -> None:
        """Adjust internal values based on parental influence."""
        self.tension += self.parent_params.get("parental_tension", 0)
        self.emotion += self.parent_params.get("parental_emotion", 0)
        self.pathos += self.parent_params.get("parental_pathos", 0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos level based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        """Check if transition thresholds are met and perform transition."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        """Advance to the next ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        base = self._generate_base_response()
        emotion = self._generate_emotional_feedback()
        return f"{base} {emotion}"

    # ------------------------------------------------------------------
    # Response helpers
    # ------------------------------------------------------------------
    def _generate_base_response(self) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def _generate_emotional_feedback(self) -> str:
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

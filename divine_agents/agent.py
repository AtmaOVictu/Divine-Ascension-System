class Agent:
    """Represents an ontological agent with dynamic transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        birth_params: dict | None = None,
        parent_params: dict | None = None,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        pathos: float = 0.0,
    ) -> None:
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

    def _apply_birth_params(self) -> None:
        """Initialize values based on birth parameters."""
        self.tension += self.birth_params.get("initial_tension", 0)
        self.emotion += self.birth_params.get("initial_emotion", 0)

    def _apply_parental_influence(self) -> None:
        """Adjust values based on parental influence."""
        self.tension += self.parent_params.get("parental_tension", 0)
        self.emotion += self.parent_params.get("parental_emotion", 0)
        self.pathos += self.parent_params.get("parental_pathos", 0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension and pathos."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self._optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for transition."""
        self.tension = value
        self._optimize_transition()

    def adjust_pathos(self, external: float) -> None:
        """Adjust pathos by an external factor."""
        self.pathos += external
        if self.pathos < 0:
            self.pathos = 0

    def _optimize_transition(self) -> None:
        """Evaluate whether a transition should occur."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        """Perform state transition and record history."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self._generate_base_response()
        emotional = self._generate_emotional_feedback()
        return f"{base} {emotional}"

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

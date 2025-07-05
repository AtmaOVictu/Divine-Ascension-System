class OntologicalAgent:
    """Agent with birth and parental influence, tension, emotion, pathos."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, birth_params: dict, parent_params: dict, state: str = "Ego"):
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion = 0.0
        self.pathos = 0.0
        self.history = [state]
        self.birth_params = birth_params
        self.parent_params = parent_params

        # Initialize from birth parameters
        self.tension += birth_params.get("initial_tension", 0)
        self.emotion += birth_params.get("initial_emotion", 0)

        self.apply_parental_influence()

    def apply_parental_influence(self) -> None:
        """Apply parental parameters on initial values."""
        self.tension += self.parent_params.get("parental_tension", 0)
        self.emotion += self.parent_params.get("parental_emotion", 0)
        self.pathos += self.parent_params.get("parental_pathos", 0)

    def update_emotion(self, value: float) -> None:
        """Update emotion and tension, adjust pathos."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        base = self.generate_response_base()
        emotional = self.generate_emotional_feedback()
        return f"{base} {emotional}"

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

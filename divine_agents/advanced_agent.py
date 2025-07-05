from __future__ import annotations
from typing import Dict, List


class AdvancedAgent:
    """Agent with birth parameters, parental influence, and dynamic dependencies."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        birth_params: Dict[str, float] | None = None,
        parent_params: Dict[str, float] | None = None,
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
        self.history: List[str] = [state]

        # Initialize from birth parameters
        self.birth_params = birth_params or {}
        self.tension += self.birth_params.get("initial_tension", 0.0)
        self.emotion += self.birth_params.get("initial_emotion", 0.0)

        # Initialize from parental influence
        self.parent_params = parent_params or {}
        self.apply_parental_influence()

    def apply_parental_influence(self) -> None:
        """Adjust initial values based on parental influence."""
        self.tension += self.parent_params.get("parental_tension", 0.0)
        self.emotion += self.parent_params.get("parental_emotion", 0.0)
        self.pathos += self.parent_params.get("parental_pathos", 0.0)

    # Public API ------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension and pathos accordingly."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level and attempt transition."""
        self.tension = value
        self.optimize_transition()

    def update_pathos(self, value: float) -> None:
        """Directly set pathos level and attempt transition."""
        self.pathos = max(0.0, value)
        self.optimize_transition()

    def respond(self, question: str) -> str:
        """Return philosophical response influenced by state and emotion."""
        base = self.generate_response_base()
        feedback = self.generate_emotional_feedback()
        return f"{base} {feedback}".strip()

    # Internal helpers ------------------------------------------------------
    def adjust_pathos(self, external_factor: float) -> None:
        self.pathos = max(0.0, self.pathos + external_factor)

    def optimize_transition(self) -> None:
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> None:
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)

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

"""Agent module implementing ontological state transitions."""

from typing import Dict, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        birth_params: Optional[Dict[str, float]] = None,
        parent_params: Optional[Dict[str, float]] = None,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        pathos: float = 0.0,
    ) -> None:
        """Initialize an agent with optional birth and parental parameters."""

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
        self.tension += self.birth_params.get("initial_tension", 0.0)
        self.emotion += self.birth_params.get("initial_emotion", 0.0)

    def _apply_parental_influence(self) -> None:
        self.tension += self.parent_params.get("parental_tension", 0.0)
        self.emotion += self.parent_params.get("parental_emotion", 0.0)
        self.pathos += self.parent_params.get("parental_pathos", 0.0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, tension and pathos."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def adjust_pathos(self, external_factor: float) -> None:
        """Modify pathos in response to an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0.0

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current emotion."""
        base_response = self._generate_response_base()
        emotional = self._generate_emotional_feedback()
        return f"{base_response} {emotional}"

    # ------------------------------------------------------------------
    # Response helpers
    # ------------------------------------------------------------------
    def _generate_response_base(self) -> str:
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

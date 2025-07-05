"""Optimized ontological agent with multidimensional transitions."""

from typing import List


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
        self.history: List[str] = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion, adjust tension and pathos, then evaluate transition."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self.optimize_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Modify pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> None:
        """Trigger a transition if any threshold is exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        """Move to the next ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Generate a response influenced by state and emotion."""
        base = self._response_base()
        emotional = self._emotional_feedback()
        return f"{base} {emotional}"

    def _response_base(self) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def _emotional_feedback(self) -> str:
        if self.emotion > 0.7:
            return "Močno čustvujem."
        if self.emotion > 0.3:
            return "Čustva rahlo vplivajo na moj odgovor."
        return "Sem miren."

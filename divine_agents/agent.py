"""Ontological agents capable of transitioning between philosophical states."""


class Agent:
    """Represents an ontological agent with dynamic parameters."""

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
        """Initialize the agent.

        Parameters
        ----------
        name:
            Identifier for the agent.
        birth_params:
            Initial conditions received at creation.
        parent_params:
            Values inherited from parents.
        state:
            Starting ontological state.
        tension, emotion, pathos:
            Initial dynamic values.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

        self.birth_params = birth_params or {}
        self.parent_params = parent_params or {}

        self.tension += self.birth_params.get("initial_tension", 0)
        self.emotion += self.birth_params.get("initial_emotion", 0)

        self.apply_parental_influence()

    def apply_parental_influence(self) -> None:
        """Adjust values based on parental influence."""
        self.tension += self.parent_params.get("parental_tension", 0)
        self.emotion += self.parent_params.get("parental_emotion", 0)
        self.pathos += self.parent_params.get("parental_pathos", 0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)
        self._maybe_transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._maybe_transition()

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos with a positive external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def _maybe_transition(self) -> None:
        """Check thresholds and perform transition if appropriate."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            self.transition()

    def transition(self) -> str:
        """Perform state transition to the next state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

from .agent import Agent


class RecursiveAgent(Agent):
    """Agent that reflects on internal state and adapts morally and emotionally."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 moral_code: str = "deontological", reflection_rate: int = 1):
        super().__init__(name, state, tension, emotion)
        self.moral_code = moral_code
        self.reflection_rate = reflection_rate
        self.emotional_state = "calm"

    def reflect(self) -> None:
        """Evaluate moral code, emotion and tension, possibly triggering transition."""
        if self.reflection_rate <= 0:
            return
        self.moral_code = self.evaluate_moral_code()
        self.emotional_state = self.evaluate_emotional_state()
        # Transition before tension is adjusted so current values are considered
        self.transition()
        self.tension = self.adjust_tension()

    # --- Evaluation helpers -------------------------------------------------
    def evaluate_moral_code(self) -> str:
        """Revise moral code based on current emotional state."""
        if self.emotional_state in ("calm", "happy"):
            return "utilitarian"
        return "deontological"

    def evaluate_emotional_state(self) -> str:
        """Determine emotional state from tension."""
        if self.tension < 5:
            return "happy"
        return "angry"

    def adjust_tension(self) -> float:
        """Adjust tension according to moral code."""
        if self.moral_code == "utilitarian":
            return max(0.0, self.tension - 1)
        return self.tension + 1

    # --- Adaptation to external input --------------------------------------
    def adapt(self, external_input: str) -> None:
        """Modify emotional state and moral code from external stimulus."""
        self.emotional_state = self.evaluate_emotional_state_based_on_input(external_input)
        self.moral_code = self.evaluate_moral_code_based_on_input(external_input)

    def evaluate_emotional_state_based_on_input(self, external_input: str) -> str:
        if external_input == "conflict":
            return "angry"
        return "calm"

    def evaluate_moral_code_based_on_input(self, external_input: str) -> str:
        if external_input == "ethical_dilemma":
            return "relativist"
        return self.moral_code

    # --- Respond ------------------------------------------------------------
    def respond(self, question: str) -> str:
        base = super().respond(question)
        if self.emotional_state == "angry":
            return base + " (jezen odgovor)"
        if self.emotional_state == "happy":
            return base + " (vesel odgovor)"
        return base

from .agent import Agent


class RecursiveAgent(Agent):
    """Agent capable of reflecting on its state and adapting."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, moral_code: str = "absolute",
                 reflection_rate: float = 1.0):
        super().__init__(name, state, tension, emotion)
        self.moral_code = moral_code
        self.reflection_rate = reflection_rate

    def reflect(self) -> None:
        """Reflect on moral code and emotional state and transition if needed."""
        if self.reflection_rate <= 0:
            return
        self.moral_code = self.evaluate_moral_code()
        self.emotion = self.evaluate_emotional_state()
        self.tension = self.adjust_tension()
        self.transition()

    def evaluate_moral_code(self) -> str:
        """Determine moral code based on current emotion."""
        if self.emotion < 0.3:
            return "absolute"
        if self.emotion < 0.7:
            return "relative"
        return "unified"

    def evaluate_emotional_state(self) -> float:
        """Revise emotion according to current tension."""
        if self.tension < 0.3:
            return 0.2
        if self.tension < 0.6:
            return 0.5
        return 0.8

    def adjust_tension(self) -> float:
        """Modify tension according to moral code."""
        if self.moral_code == "absolute":
            return max(self.tension - 0.1, 0.0)
        if self.moral_code == "relative":
            return self.tension
        return min(self.tension + 0.1, 1.0)

    def adapt(self, external_input: str) -> None:
        """Adapt to external input then reflect."""
        self.emotion = self.evaluate_emotional_state_based_on_input(external_input)
        self.moral_code = self.evaluate_moral_code_based_on_input(external_input)
        self.reflect()

    def evaluate_emotional_state_based_on_input(self, external_input: str) -> float:
        if external_input == "conflict":
            return min(self.emotion + 0.4, 1.0)
        return max(self.emotion - 0.2, 0.0)

    def evaluate_moral_code_based_on_input(self, external_input: str) -> str:
        if external_input == "ethical_dilemma":
            return "relative"
        return self.moral_code

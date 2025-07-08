import time
from typing import Any, Dict, List

from .agent import Agent


class RecursiveAgent(Agent):
    """Agent with basic reflection abilities."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, reflection_rate: float = 1.0) -> None:
        super().__init__(name, state, tension, emotion)
        self.reflection_rate = reflection_rate

    def reflect(self) -> str:
        """Reflect on past actions and adjust tension."""
        self.tension *= max(0.0, 1 - 0.1 * self.reflection_rate)
        return self.transition()

    def adapt(self, external_input: Any) -> str:
        """Adapt to new input by updating emotion."""
        self.update_emotion(min(1.0, self.emotion + 0.1))
        return self.reflect()


class DataCompliantRecursiveAgent(RecursiveAgent):
    """RecursiveAgent that tracks data usage for compliance."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, reflection_rate: float = 1.0,
                 data_compliance: str = "enabled") -> None:
        super().__init__(name, state, tension, emotion, reflection_rate)
        self.data_compliance = data_compliance
        self.usage_log: List[Dict[str, Any]] = []

    def track_data_usage(self, data_type: str, data_source: Any) -> None:
        if self.data_compliance == "enabled":
            entry = {
                "agent": self.name,
                "data_type": data_type,
                "data_source": data_source,
                "timestamp": time.time(),
            }
            self.log_data_usage(entry)

    def log_data_usage(self, entry: Dict[str, Any]) -> None:
        self.usage_log.append(entry)

    def reflect(self) -> str:
        self.track_data_usage("reflection", "internal")
        return super().reflect()

    def adapt(self, external_input: Any) -> str:
        self.track_data_usage("external_input", external_input)
        return super().adapt(external_input)

    def evaluate_emotional_state_based_on_input(self, external_input: Any) -> float:
        self.track_data_usage("emotional_state_adjustment", external_input)
        if str(external_input).lower() in {"praise", "joy"}:
            self.update_emotion(0.3)
        else:
            self.update_emotion(0.6)
        return self.emotion

    def evaluate_moral_code_based_on_input(self, external_input: Any) -> str:
        self.track_data_usage("moral_code_adjustment", external_input)
        return "ethical"

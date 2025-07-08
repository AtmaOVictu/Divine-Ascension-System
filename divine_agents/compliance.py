"""Data compliant recursive agents."""

from __future__ import annotations

import time
from typing import Any, Dict, List

from .agent import Agent


class DataCompliantRecursiveAgent(Agent):
    """Agent that logs data usage during reflection and adaptation."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        reflection_rate: float = 0.0,
        data_compliance: str = "enabled",
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.reflection_rate = reflection_rate
        self.data_compliance = data_compliance
        self.data_usage_log: List[Dict[str, Any]] = []

    def log_data_usage(self, entry: Dict[str, Any]) -> None:
        """Store a log entry for later inspection."""
        self.data_usage_log.append(entry)

    def track_data_usage(self, data_type: str, data_source: Any) -> None:
        """Record data access for transparency and accountability."""
        if self.data_compliance == "enabled":
            entry = {
                "agent": self.name,
                "data_type": data_type,
                "data_source": data_source,
                "timestamp": time.time(),
            }
            self.log_data_usage(entry)

    def reflect(self) -> None:
        """Reflect on past actions, reducing tension and logging usage."""
        self.track_data_usage("reflection", "internal")
        if self.reflection_rate > 0:
            self.tension = max(0.0, self.tension - self.reflection_rate)

    def adapt(self, external_input: Any) -> None:
        """Adapt to external input while tracking usage."""
        self.track_data_usage("external_input", external_input)
        # Increase emotion substantially to trigger potential transitions
        self.update_emotion(min(1.0, self.emotion + 0.8))

    def evaluate_emotional_state_based_on_input(self, external_input: Any) -> float:
        """Return a tentative new emotion influenced by the input."""
        self.track_data_usage("emotional_state_adjustment", external_input)
        return min(1.0, self.emotion + 0.1)

    def evaluate_moral_code_based_on_input(self, external_input: Any) -> str:
        """Produce a placeholder moral evaluation while logging usage."""
        self.track_data_usage("moral_code_adjustment", external_input)
        return f"moral-eval-{external_input}"


from __future__ import annotations
import time
from typing import Dict, Any, List

from .agent import Agent


class DataCompliantAgent(Agent):
    """Agent with data compliance logging for transparency and accountability."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 data_compliance: str = "disabled") -> None:
        super().__init__(name, state, tension, emotion)
        self.data_compliance = data_compliance
        self.usage_log: List[Dict[str, Any]] = []

    def track_data_usage(self, data_type: str, data_source: str) -> None:
        """Record data usage events if compliance logging is enabled."""
        if self.data_compliance == "enabled":
            entry = {
                "agent": self.name,
                "data_type": data_type,
                "data_source": data_source,
                "timestamp": time.time(),
            }
            self.log_data_usage(entry)

    def log_data_usage(self, entry: Dict[str, Any]) -> None:
        """Persist usage entries for later inspection."""
        self.usage_log.append(entry)

    def reflect(self) -> str:
        """Reflect on actions while logging compliance details."""
        self.track_data_usage("reflection", "internal_decision_making")
        return super().respond("Kaj je resnica?")

    def adapt(self, external_input: str) -> str:
        """Adapt to new input with compliance tracking."""
        self.track_data_usage("external_input", external_input)
        self.update_emotion(min(self.emotion + 0.1, 1.0))
        return self.transition()

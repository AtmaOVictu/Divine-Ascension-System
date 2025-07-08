import time
from .agent import Agent


class DataCompliantAgent(Agent):
    """Agent that logs data usage for compliance."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, data_compliance: bool = True):
        super().__init__(name, state, tension, emotion)
        self.data_compliance = data_compliance
        self.usage_logs = []

    def track_data_usage(self, data_type: str, data_source: str) -> None:
        """Log data usage if compliance is enabled."""
        if self.data_compliance:
            entry = {
                "agent": self.name,
                "state": self.state,
                "data_type": data_type,
                "data_source": data_source,
                "timestamp": time.time(),
            }
            self.log_data_usage(entry)

    def log_data_usage(self, entry: dict) -> None:
        """Store usage logs for accountability."""
        self.usage_logs.append(entry)

    def reflect(self) -> None:
        """Reflect on actions while tracking data usage."""
        self.track_data_usage("reflection", "internal")
        self.transition()

    def adapt(self, external_input: str) -> None:
        """Adapt to external input with compliance tracking."""
        self.track_data_usage("external_input", external_input)
        # Example adaptation: update emotion based on external input length
        self.update_emotion(min(len(external_input) / 10.0, 1.0))
        self.transition()

    def evaluate_emotional_state_based_on_input(self, external_input: str) -> None:
        """Adjust emotional state while logging data usage."""
        self.track_data_usage("emotional_state_adjustment", external_input)
        self.update_emotion(min(len(external_input) / 20.0, 1.0))

    def evaluate_moral_code_based_on_input(self, external_input: str) -> None:
        """Placeholder for moral code evaluation with compliance logging."""
        self.track_data_usage("moral_code_adjustment", external_input)


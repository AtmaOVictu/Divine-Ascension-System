from dataclasses import dataclass


@dataclass
class NanoMoment:
    """Represents a microscopic change influencing an agent."""
    value: float

    def apply(self, agent) -> None:
        """Apply nano moment to an agent by adjusting emotion and tension."""
        agent.update_emotion(self.value)


@dataclass
class MegaMoment:
    """Represents a macroscopic change triggered by accumulated nano moments."""
    threshold: float = 1.5
    accumulated: float = 0.0

    def accumulate(self, nano: NanoMoment) -> None:
        self.accumulated += nano.value

    def trigger(self, agent) -> None:
        """Trigger a state transition if accumulated value exceeds threshold."""
        if self.accumulated >= self.threshold:
            agent.transition()
            self.accumulated = 0.0

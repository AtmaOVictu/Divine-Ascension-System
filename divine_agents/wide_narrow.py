from typing import Dict, List
from .agent import Agent


class WideAgent(Agent):
    """Agent with support for multiple dimensions and flexible behaviour."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.dimensions: Dict[str, float] = {
            "space": 0.0,
            "time": 0.0,
            "emotion": self.emotion,
        }

    def update_dimension(self, key: str, value: float) -> None:
        """Update one of the tracked dimensions."""
        self.dimensions[key] = value


class NarrowAgent(Agent):
    """Specialised agent that reacts when tension exceeds a threshold."""

    def __init__(self, name: str, threshold: float = 0.5, **kwargs):
        super().__init__(name, **kwargs)
        self.threshold = threshold
        self.action_triggered = False

    def check_threshold(self) -> None:
        """Trigger an action if tension is above the threshold."""
        if self.tension > self.threshold:
            self.perform_action()

    def perform_action(self) -> None:
        """Record that the threshold has been exceeded."""
        self.action_triggered = True


def debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a short philosophical debate between two agents."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines

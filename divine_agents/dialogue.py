from typing import List
from .agent import Agent


class DialogueManager:
    """Manage dialogue and emotional transitions between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> List[str]:
        """Advance the dialogue by updating emotions and returning responses."""
        self.agent1.update_emotion(emotion1)
        self.agent1.transition()
        self.agent2.update_emotion(emotion2)
        self.agent2.transition()

        line1 = f"{self.agent1.name} ({self.agent1.state}): {self.agent1.speak()}"
        line2 = f"{self.agent2.name} ({self.agent2.state}): {self.agent2.speak()}"
        self.history.extend([line1, line2])
        return [line1, line2]


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue using :class:`DialogueManager`."""
    manager = DialogueManager(agent1, agent2)
    lines = []
    lines.extend(manager.step(0.8, 0.6))
    lines.extend(manager.step(0.0, 0.0))
    return lines

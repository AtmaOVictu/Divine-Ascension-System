from typing import List, Tuple

from .agent import Agent


class Discourse:
    """Manage a philosophical discourse between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, emotions: Tuple[float, float]) -> None:
        """Perform one step of dialogue updating emotions and states."""
        e1, e2 = emotions
        self.agent1.update_emotion(e1)
        self.agent1.transition()
        self.agent2.update_emotion(e2)
        self.agent2.transition()

        self.history.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        self.history.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

    def run(self, emotion_sequence: List[Tuple[float, float]]) -> List[str]:
        """Run a sequence of discourse steps with given emotions."""
        for emotions in emotion_sequence:
            self.step(emotions)
        return self.history

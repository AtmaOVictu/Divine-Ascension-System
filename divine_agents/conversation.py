from typing import Iterable, List, Tuple

from .agent import Agent


class Conversation:
    """Manage philosophical dialogue and state transitions between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.lines: List[str] = []

    def _record(self, line: str) -> None:
        self.lines.append(line)

    def _exchange(self) -> None:
        self._record(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        self._record(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

    def _apply_emotions(self, emotion1: float, emotion2: float) -> None:
        self.agent1.update_emotion(self.agent1.emotion + emotion1)
        self._record(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
        self._record(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )

        self.agent2.update_emotion(self.agent2.emotion + emotion2)
        self._record(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")
        self._record(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

    def interact(self, emotion1: float, emotion2: float) -> None:
        """Perform one interaction step with emotion updates."""
        self._exchange()
        self._apply_emotions(emotion1, emotion2)

    def run(self, emotion_steps: Iterable[Tuple[float, float]]) -> List[str]:
        for e1, e2 in emotion_steps:
            self.interact(e1, e2)
        return self.lines

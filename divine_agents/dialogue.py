"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a simple philosophical dialogue between two agents."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


class DialogueManager:
    """Manage dynamic dialogues and state transitions between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2

    def exchange(self, emotion1: float, emotion2: float) -> List[str]:
        """Perform one exchange updating emotions and states."""
        self.agent1.update_emotion(emotion1)
        self.agent2.update_emotion(emotion2)

        lines = [
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}",
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}",
        ]

        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")
        return lines

    def run_dialogue(self, emotions1: List[float], emotions2: List[float]) -> List[str]:
        """Run multiple exchanges between agents."""
        transcript: List[str] = []
        for e1, e2 in zip(emotions1, emotions2):
            transcript.extend(self.exchange(e1, e2))
        return transcript

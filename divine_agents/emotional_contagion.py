from __future__ import annotations

from .agent import Agent


class EmotionalContagion:
    """Spread emotions between agents."""

    def __init__(self) -> None:
        self.agents: list[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def spread_emotion(self, agent_index: int, emotion_influence: float) -> None:
        """Propagate the selected agent's emotion to others."""
        if not (0 <= agent_index < len(self.agents)):
            raise IndexError("agent_index out of range")
        source = self.agents[agent_index]
        for i, other in enumerate(self.agents):
            if i == agent_index:
                continue
            other.update_emotion(source.emotion + emotion_influence)


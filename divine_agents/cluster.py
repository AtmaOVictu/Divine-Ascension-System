from __future__ import annotations

from typing import List

from .agent import Agent


class AgentCluster:
    """Manage a group of agents that influence each other's evolution."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.cluster_state: str = "Unformed"

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the cluster."""
        self.agents.append(agent)

    def transition_agents(self) -> None:
        """Trigger transitions for all agents."""
        for agent in self.agents:
            agent.transition()

    def synchronize_emotions(self) -> None:
        """Align emotions across all agents."""
        if not self.agents:
            return
        avg = sum(a.emotion for a in self.agents) / len(self.agents)
        for agent in self.agents:
            agent.update_emotion(avg)

    def update_cluster_state(self) -> None:
        """Set cluster state based on all agent states."""
        if self.agents and all(a.state == "Enotnost" for a in self.agents):
            self.cluster_state = "Unified"
        else:
            self.cluster_state = "In Progress"

    def report_cluster_status(self) -> str:
        """Return a textual summary of the cluster."""
        lines = [f"Cluster State: {self.cluster_state}"]
        for a in self.agents:
            lines.append(f"{a.name}: {a.state}, Emotion: {a.emotion:.2f}")
        return "\n".join(lines)

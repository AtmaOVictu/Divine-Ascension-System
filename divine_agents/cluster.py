from __future__ import annotations

from typing import List

from .agent import Agent


class AgentCluster:
    """Manage a group of interacting agents."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.cluster_state: str = "Unformed"

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the cluster."""
        self.agents.append(agent)

    def transition_agents(self) -> None:
        """Transition all agents within the cluster."""
        for agent in self.agents:
            agent.transition()

    def synchronize_emotions(self) -> None:
        """Synchronize emotions across all agents."""
        if not self.agents:
            return
        avg = sum(a.emotion for a in self.agents) / len(self.agents)
        for agent in self.agents:
            agent.update_emotion(avg)

    def update_cluster_state(self) -> None:
        """Update the cluster state based on agent states."""
        if self.agents and all(a.state == "Enotnost" for a in self.agents):
            self.cluster_state = "Unified"
        else:
            self.cluster_state = "In Progress"

    def report_cluster_status(self) -> str:
        """Return a text summary of the cluster's state."""
        lines = [f"Cluster State: {self.cluster_state}"]
        for agent in self.agents:
            lines.append(f"{agent.name}: {agent.state}, Emotion: {agent.emotion}")
        return "\n".join(lines)

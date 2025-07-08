from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .agent import Agent


@dataclass
class AgentCluster:
    """Manage a collection of agents that evolve together."""

    agents: List[Agent] = field(default_factory=list)
    cluster_state: str = "Unformed"

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the cluster."""
        self.agents.append(agent)

    def transition_agents(self) -> None:
        """Transition all agents based on their tension and emotion."""
        for agent in self.agents:
            agent.transition()
        self.update_cluster_state()

    def synchronize_emotions(self) -> None:
        """Synchronize emotional state across all agents."""
        if not self.agents:
            return
        avg_emotion = sum(a.emotion for a in self.agents) / len(self.agents)
        for agent in self.agents:
            agent.update_emotion(avg_emotion)

    def update_cluster_state(self) -> None:
        """Update the cluster state based on agent progress."""
        if self.agents and all(agent.state == "Enotnost" for agent in self.agents):
            self.cluster_state = "Unified"
        else:
            self.cluster_state = "In Progress"

    def report_cluster_status(self) -> List[str]:
        """Return a summary of the cluster's status."""
        report = [f"Cluster State: {self.cluster_state}"]
        for agent in self.agents:
            report.append(f"{agent.name}: {agent.state}, Emotion: {agent.emotion:.2f}")
        return report

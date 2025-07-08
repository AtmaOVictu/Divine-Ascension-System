from __future__ import annotations

from .agent import Agent


class ReputationSystem:
    """Handle fame changes based on interactions between agents."""

    def interact(self, agent1: Agent, agent2: Agent, action: str) -> None:
        """Adjust fame of agents based on the supplied action."""
        if action == "help":
            agent1.update_fame(2, 0, 5)
            agent2.update_fame(2, 0, 5)
        elif action == "betray":
            agent1.update_fame(0, 3, 0)
            agent2.update_fame(0, 0, 0)


def social_influence(agent: Agent, target: Agent) -> bool:
    """Return ``True`` if ``agent`` can influence ``target`` based on fame."""
    if agent.fame > target.fame:
        return True
    return False

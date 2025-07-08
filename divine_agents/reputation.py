from .agent import Agent


class ReputationSystem:
    """Handle inter-agent interactions and their fame effects."""

    def __init__(self) -> None:
        self.agent_interactions = {}

    def interact(self, agent1: Agent, agent2: Agent, action: str) -> None:
        """Influence fame based on interaction type."""
        if action == "help":
            agent1.update_fame(positive_actions=2, negative_actions=0, participation_score=5)
            agent2.update_fame(positive_actions=2, negative_actions=0, participation_score=5)
        elif action == "betray":
            agent1.update_fame(positive_actions=0, negative_actions=3, participation_score=0)
            agent2.update_fame(positive_actions=0, negative_actions=0, participation_score=0)

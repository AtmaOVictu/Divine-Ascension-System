class ReputationSystem:
    """Manage interactions between agents and adjust fame accordingly."""

    def interact(self, agent1, agent2, action: str) -> None:
        """Apply fame changes based on the interaction type."""
        if action == "help":
            agent1.update_fame(positive_actions=2, participation_score=5)
            agent2.update_fame(positive_actions=2, participation_score=5)
        elif action == "betray":
            agent1.update_fame(negative_actions=3)
            # agent2 gets no fame change for being betrayed
        else:
            raise ValueError(f"Unknown action: {action}")

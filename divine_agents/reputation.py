class ReputationSystem:
    """Manage inter-agent interactions affecting fame."""

    def interact(self, agent1, agent2, action: str) -> None:
        """Influence agents' fame based on an action."""
        if action == "help":
            agent1.update_fame(positive_actions=2, negative_actions=0,
                               participation_score=5)
            agent2.update_fame(positive_actions=2, negative_actions=0,
                               participation_score=5)
        elif action == "betray":
            agent1.update_fame(positive_actions=0, negative_actions=3,
                               participation_score=0)
            agent2.update_fame(positive_actions=0, negative_actions=0,
                               participation_score=0)

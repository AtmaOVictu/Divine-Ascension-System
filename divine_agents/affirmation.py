class Affirmation:
    """Handles affirmation processes for agents."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        """Affirm the agent's current state as existing."""
        message = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(message)
        return message

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        """Affirm the agent's transition into its current state."""
        message = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(message)
        return message

class Affirmation:
    """Utility class providing affirmation messages."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        """Affirm the agent's current state as proof of existence."""
        message = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(message)
        return message

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        """Affirm the agent's transition to a new state."""
        message = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(message)
        return message

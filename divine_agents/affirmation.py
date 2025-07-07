class Affirmation:
    """Utility methods for affirming agent existence and transitions."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        """Affirm the agent's current state as a confirmation of existence."""
        message = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(message)
        print(message)
        return message

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        """Affirm the agent's state transition."""
        message = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(message)
        print(message)
        return message

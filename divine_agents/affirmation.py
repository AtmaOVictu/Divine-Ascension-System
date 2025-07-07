class Affirmation:
    """Utility methods for affirming agent existence and transitions."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        message = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(message)
        return message

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        message = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(message)
        return message

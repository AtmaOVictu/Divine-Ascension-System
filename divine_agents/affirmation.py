class Affirmation:
    """Utility to record and return affirmation messages."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        """Affirm that the agent exists in its current state."""
        msg = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(msg)
        return msg

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        """Affirm that the agent has transitioned to a new state."""
        msg = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(msg)
        return msg

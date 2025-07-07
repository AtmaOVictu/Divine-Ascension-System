class Affirmation:
    """Represents a process of affirmation in an ontological system."""

    @staticmethod
    def affirm_existence(agent: 'Agent') -> str:
        """Affirm the agent's current state."""
        message = f"Affirmation: {agent.name} exists in state {agent.state}."
        agent.history.append(message)
        return message

    @staticmethod
    def affirm_transition(agent: 'Agent') -> str:
        """Affirm the agent's recent transition."""
        message = f"Affirmation: {agent.name} transitioned to {agent.state}."
        agent.history.append(message)
        return message


class Negation:
    """Represents necessary negation leading to transformation."""

    @staticmethod
    def negate_state(agent: 'Agent') -> str:
        """Negate the agent's current state and shift accordingly."""
        message = f"Negation: {agent.name} negated its state {agent.state}."
        agent.history.append(message)
        if agent.state == "Ego":
            agent.state = "Enotnost"
        elif agent.state == "Jaz":
            agent.state = "Ego"
        agent.history.append(f"New state after negation: {agent.state}")
        return agent.state

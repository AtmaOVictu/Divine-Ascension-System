class Negation:
    """Handles necessary negation to trigger state shifts."""

    @staticmethod
    def negate_state(agent: 'Agent') -> str:
        """Negate the agent's state, updating it accordingly."""
        message = f"Negation: {agent.name} negated its state {agent.state}."
        agent.history.append(message)
        if agent.state == "Ego":
            agent.state = "Enotnost"
        elif agent.state == "Jaz":
            agent.state = "Ego"
        agent.history.append(f"New state after negation: {agent.state}")
        return agent.state

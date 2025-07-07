from .agent import Agent

class Affirmation:
    """Process of affirmation in the ontological system."""

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


class Negation:
    """Necessary negation enabling dynamic change."""

    @staticmethod
    def negate_state(agent: 'Agent') -> str:
        message = f"Negation: {agent.name} negated its state {agent.state}."
        agent.history.append(message)
        if agent.state == "Ego":
            agent.state = "Enotnost"
        elif agent.state == "Jaz":
            agent.state = "Ego"
        agent.history.append(f"New state after negation: {agent.state}")
        return agent.state

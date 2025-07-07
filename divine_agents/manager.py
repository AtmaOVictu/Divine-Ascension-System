class SubAgent:
    """A helper that logs actions for its associated agent."""

    def __init__(self, name: str, associated_agent: 'Agent'):
        self.name = name
        self.associated_agent = associated_agent
        self.logs = []

    def log_action(self, action: str) -> None:
        entry = f"{self.name}: {action}"
        self.logs.append(entry)


class ManagerAgent:
    """Coordinates a collection of agents and manages their transitions."""

    def __init__(self, name: str):
        self.name = name
        self.agents = []

    def add_agent(self, agent: 'Agent') -> None:
        self.agents.append(agent)

    def manage_transitions(self) -> None:
        for agent in self.agents:
            agent.transition()

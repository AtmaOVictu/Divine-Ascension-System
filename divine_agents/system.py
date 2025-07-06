class Module:
    """Container for agents sharing a common ontological state."""

    def __init__(self, name: str):
        self.name = name
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)


class DynamicAgentSystem:
    """Manage multiple modules and handle agent transitions across them."""

    def __init__(self):
        from .agent import Agent  # Local import to avoid circular imports
        self.modules = {state: Module(state) for state in Agent.STATES}

    def add_agent(self, agent):
        self.modules[agent.state].add_agent(agent)

    def step(self):
        """Update all agents once and move them between modules if state changes."""
        all_agents = [agent for module in self.modules.values() for agent in module.agents]
        for agent in all_agents:
            current_module = self.modules[agent.state]
            old_state = agent.state
            agent.transition()
            if agent.state != old_state:
                current_module.remove_agent(agent)
                self.modules[agent.state].add_agent(agent)

    def summary(self):
        """Return a summary of agent distribution across modules."""
        return {
            name: [agent.name for agent in module.agents]
            for name, module in self.modules.items()
        }

class SubAgent:
    """Responsible for sorting and managing agent logs."""

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        """Add an agent to be managed."""
        self.agents.append(agent)

    def sort_logs_by_version(self):
        """Return agents sorted by version timestamp."""
        return sorted(self.agents, key=lambda a: a.version)

    def save_all_logs(self):
        """Save history logs for all managed agents."""
        for agent in self.agents:
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")

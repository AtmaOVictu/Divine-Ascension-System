class SubAgent:
    """Responsible for sorting and managing agent logs."""

    def __init__(self):
        self.agents_logs = {}

    def add_agent(self, agent):
        """Register an agent for log management."""
        self.agents_logs[agent.name] = agent

    def sort_logs_by_version(self):
        """Return agents sorted by their version timestamp."""
        return sorted(self.agents_logs.values(), key=lambda a: a.version)

    def save_all_logs(self):
        """Invoke history saving on all managed agents."""
        for agent in self.agents_logs.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")


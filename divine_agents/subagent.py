class SubAgent:
    """Manage multiple agents and their logs."""

    def __init__(self):
        self.agents_logs = {}

    def add_agent(self, agent):
        """Store an agent for management."""
        self.agents_logs[agent.name] = agent

    def sort_logs_by_version(self):
        """Return agents sorted by creation timestamp."""
        return sorted(self.agents_logs.values(), key=lambda a: a.timestamp)

    def save_all_logs(self):
        """Persist histories for all managed agents."""
        for agent in self.agents_logs.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")


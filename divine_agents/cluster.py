class AgentCluster:
    """Manage a group of agents and their collective evolution."""

    def __init__(self):
        self.agents = []
        self.cluster_state = "Unformed"

    def add_agent(self, agent):
        """Add an agent to the cluster."""
        self.agents.append(agent)

    def transition_agents(self):
        """Trigger transitions for all agents."""
        for agent in self.agents:
            agent.transition()

    def synchronize_emotions(self):
        """Synchronize emotional states across the cluster."""
        if not self.agents:
            return
        avg_emotion = sum(a.emotion for a in self.agents) / len(self.agents)
        for agent in self.agents:
            agent.update_emotion(avg_emotion)

    def update_cluster_state(self):
        """Update cluster state based on agents' collective progress."""
        if self.agents and all(a.state == "Enotnost" for a in self.agents):
            self.cluster_state = "Unified"
        else:
            self.cluster_state = "In Progress"

    def report_cluster_status(self):
        """Return a textual status of the cluster."""
        report = [f"Cluster State: {self.cluster_state}"]
        for agent in self.agents:
            report.append(f"{agent.name}: {agent.state}, Emotion: {agent.emotion}")
        return report

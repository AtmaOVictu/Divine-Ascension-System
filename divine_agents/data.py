class DataHarvester:
    """Collects contextual data from agents for future analysis."""

    def __init__(self):
        self.data = []

    def collect_data(self, agent, event: str) -> None:
        """Store agent information and related event."""
        self.data.append({
            "agent": agent.name,
            "state": agent.state,
            "tension": agent.tension,
            "emotion": agent.emotion,
            "event": event,
        })

    def send_data(self):
        """Return all collected data."""
        return list(self.data)

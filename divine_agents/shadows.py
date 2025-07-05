class UrgentShadow:
    """Represents an urgent shadow forcing an agent to confront tension."""

    def __init__(self, name: str, urgency: float):
        self.name = name
        self.urgency = urgency

    def trigger(self, agent) -> None:
        """Increase agent tension if urgency threshold is met."""
        if self.urgency >= 0.8:
            agent.update_tension(max(agent.tension, self.urgency))

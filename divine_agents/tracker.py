class Tracker:
    """Simple tracker that logs agent states over time."""

    def __init__(self) -> None:
        self.log = {}

    def track(self, agent) -> None:
        self.log.setdefault(agent.name, []).append(agent.state)

    def history(self, name: str):
        return self.log.get(name, [])

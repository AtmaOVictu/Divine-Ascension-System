class TimeManager:
    """Manage different layers of time for agents."""

    def __init__(self) -> None:
        self.absolute_time = 0.0
        self.meta_time = 1.0
        self.god_time = 1.0
        self.history = []

    def update_time(self, agent) -> None:
        """Update time flow based on the agent's emotional and ontological state."""
        if agent.tension > 0.7:
            self.meta_time = 0.5
        elif agent.tension < 0.3:
            self.meta_time = 1.5
        else:
            self.meta_time = 1.0

        self.absolute_time += self.meta_time * self.god_time
        self.history.append(self.absolute_time)

        if agent.state == "Enotnost":
            self.god_time = 0.8
        elif agent.state == "Jaz":
            self.god_time = 1.0
        else:
            self.god_time = 1.2

    def report(self) -> dict:
        """Return the current time status."""
        return {
            "absolute_time": self.absolute_time,
            "meta_time": self.meta_time,
            "god_time": self.god_time,
            "history": list(self.history),
        }

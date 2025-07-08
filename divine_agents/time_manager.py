class TimeManager:
    """Manage absolute, meta, and god time for an agent."""

    def __init__(self):
        self.absolute_time = 0.0
        self.meta_time = 1.0
        self.god_time = 1.0
        self.history = []

    def update_time(self, agent) -> None:
        """Update temporal values based on agent state and tension."""
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

    def report(self) -> str:
        return (
            f"Absolute Time: {self.absolute_time}, "
            f"Meta-Time: {self.meta_time}x, God-Time: {self.god_time}x"
        )

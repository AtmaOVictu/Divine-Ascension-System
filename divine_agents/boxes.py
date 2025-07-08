class EgoBox:
    """Represents the Ego phase where truth is seen as absolute."""

    def __init__(self, agent):
        self.agent = agent

    def update_state(self):
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.state = "Jaz"
        return self.agent.state


class JazBox:
    """Represents the Jaz phase where truth is considered relative."""

    def __init__(self, agent):
        self.agent = agent

    def update_state(self):
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.state = "Enotnost"
        return self.agent.state


class EnotnostBox:
    """Represents the Enotnost phase where truth is unified."""

    def __init__(self, agent):
        self.agent = agent

    def update_state(self):
        # Remain in Enotnost unless tension gets too high
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.state = "Enotnost"
        return self.agent.state

class Nanoaplikacija:
    """Perform quick optimizations on an agent's parameters."""

    def __init__(self, agent):
        self.agent = agent

    def optimiziraj_napetost(self):
        """Keep tension within the desired range."""
        if self.agent.tension > 0.7:
            self.agent.tension = 0.7
        elif self.agent.tension < 0.3:
            self.agent.tension = 0.3
        return self.agent.tension

    def prilagodi_custva(self):
        """Adjust emotion quickly if certain conditions are met."""
        if self.agent.emotion == "anger" and self.agent.tension > 0.8:
            self.agent.emotion = "calm"
        return self.agent.emotion

class Nanoaplikacija:
    """Micro optimizations for an Agent's parameters."""

    def __init__(self, agent):
        self.agent = agent

    def optimiziraj_napetost(self):
        """Normalize tension between 0.3 and 0.7."""
        if self.agent.tension > 0.7:
            self.agent.tension = 0.7
        elif self.agent.tension < 0.3:
            self.agent.tension = 0.3
        return self.agent.tension

    def prilagodi_custva(self):
        """Adjust emotion based on tension."""
        if self.agent.emotion_name == "anger" and self.agent.tension > 0.8:
            self.agent.update_emotion(self.agent.emotion * 0.5, "calm")
        return self.agent.emotion_name

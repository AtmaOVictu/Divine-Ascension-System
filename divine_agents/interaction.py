class Interakcije:
    """Model mutual influence between two agents."""

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    def medsebojna_interakcija(self):
        """Adjust tension based on emotional states."""
        if self.agent1.emotion == "anger" and self.agent2.emotion == "calm":
            self.agent2.tension += 0.2
        elif self.agent1.emotion == "calm" and self.agent2.emotion == "anger":
            self.agent1.tension += 0.2

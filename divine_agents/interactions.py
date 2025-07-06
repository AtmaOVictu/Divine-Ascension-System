class Interakcije:
    """Mutual influence on tension and emotion between two agents."""

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    def medsebojna_interakcija(self):
        if self.agent1.emotion_name == "anger" and self.agent2.emotion_name == "calm":
            self.agent2.tension += 0.2
        elif self.agent1.emotion_name == "calm" and self.agent2.emotion_name == "anger":
            self.agent1.tension += 0.2

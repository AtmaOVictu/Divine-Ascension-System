class MultiLayeredAgent:
    """Wrap an Agent to handle multi-layer transitions."""

    def __init__(self, agent):
        self.agent = agent

    def multi_layer_transition(self):
        emotion_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = getattr(self.agent, 'loyalty', 0.5)
        experience_layer = self.agent.experiences[-1] if getattr(self.agent, 'experiences', []) else 'neutral'

        if self.agent.state == 'Ego' and (tension_layer > 0.7 or emotion_layer > 0.5 or emotion_layer == 'fearful'):
            self.agent.state = 'Jaz'
        elif self.agent.state == 'Jaz' and (loyalty_layer > 0.8 or 'selfish' in experience_layer):
            self.agent.state = 'Enotnost'
        self.agent.history.append(self.agent.state)
        return self.agent.state


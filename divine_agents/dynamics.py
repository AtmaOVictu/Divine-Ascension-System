class EmotionalTensionDynamics:
    """Adjust tension based on the agent's emotional state."""

    def __init__(self, agent):
        self.agent = agent

    def adjust_tension(self):
        emotion = getattr(self.agent, 'emotion', 0.0)
        if emotion == 'angry':
            self.agent.tension += 0.3
        elif emotion == 'happy':
            self.agent.tension -= 0.2
        elif emotion == 'fear':
            self.agent.tension += 0.4
        else:
            self.agent.tension += 0.1
        # Clamp tension within 0-1 for simplicity
        self.agent.tension = max(0.0, min(1.0, self.agent.tension))
        return self.agent.tension


class GranularniPrehodi:
    """Manage complex state transitions based on multiple factors."""

    def __init__(self, agent):
        self.agent = agent

    def prehod(self, emotion: str, tension: float, history):
        """Transition agent state based on emotion and tension."""
        if tension > 0.8 and emotion == "anger":
            self.agent.state = "Jaz"
        elif emotion == "calm" and tension < 0.3:
            self.agent.state = "Enotnost"
        else:
            self.agent.state = "Ego"
        self.agent.history.append(self.agent.state)
        return self.agent.state

class GranularniPrehodi:
    """Handle more nuanced state transitions for an Agent."""

    def __init__(self, agent):
        self.agent = agent

    def prehod(self, emotion: float, tension: float):
        """Transition between states based on emotion and tension."""
        self.agent.update_emotion(emotion)
        self.agent.update_tension(tension)
        return self.agent.transition()

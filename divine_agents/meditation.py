from .agent import Agent

class Meditation:
    """Introspective process increasing emotional awareness."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def reflect(self) -> str:
        """Raise emotion to trigger potential state transition."""
        # Meditation increases emotion, leading to inner change
        self.agent.update_emotion(0.6)
        return self.agent.transition()

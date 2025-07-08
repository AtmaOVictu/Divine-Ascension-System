from .agent import Agent
class Environment:
    """External conditions influencing agents."""

    def __init__(self, tension_modifier: float = 0.0, emotion_modifier: float = 0.0):
        self.tension_modifier = tension_modifier
        self.emotion_modifier = emotion_modifier

    def influence(self, agent: Agent) -> None:
        """Apply environmental effects to an agent."""
        new_emotion = min(1.0, agent.emotion + self.emotion_modifier)
        agent.update_emotion(new_emotion)
        agent.update_tension(agent.tension + self.tension_modifier)


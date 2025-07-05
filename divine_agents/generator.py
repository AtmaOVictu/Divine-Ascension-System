class Generator:
    """Influences agents by adjusting tension and emotion."""

    def __init__(self, tension_boost: float = 0.0, emotion_boost: float = 0.0):
        self.tension_boost = tension_boost
        self.emotion_boost = emotion_boost

    def stimulate(self, agent: "Agent") -> None:
        """Apply boosts to an agent's tension and emotion."""
        from .agent import Agent  # local import to avoid circular dependency
        if not isinstance(agent, Agent):
            raise TypeError("Expected Agent instance")
        agent.update_tension(agent.tension + self.tension_boost)
        new_emotion = min(1.0, agent.emotion + self.emotion_boost)
        agent.update_emotion(new_emotion)

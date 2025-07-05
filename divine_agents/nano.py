class Nano:
    """Basic unit representing a micro transition affecting emotion or tension."""

    def __init__(self, emotion_delta: float = 0.0, tension_delta: float = 0.0):
        self.emotion_delta = emotion_delta
        self.tension_delta = tension_delta

    def apply(self, agent: 'Agent') -> None:
        """Apply nano adjustments to the given agent."""
        # adjust emotion first so tension calculation is correct
        if self.emotion_delta:
            agent.update_emotion(agent.emotion + self.emotion_delta)
        if self.tension_delta:
            agent.update_tension(agent.tension + self.tension_delta)

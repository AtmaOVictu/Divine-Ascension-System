class TransitionVerifier:
    """Verify and analyze state transitions for an agent."""

    def __init__(self, agent, tension_threshold=0.7, emotion_threshold=0.5):
        self.agent = agent
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold

    def verify_transition(self):
        """Trigger agent transition if thresholds are met."""
        if (self.agent.tension >= self.tension_threshold or
                self.agent.emotion >= self.emotion_threshold):
            return self.agent.transition()
        return self.agent.state

    def seciraj(self):
        """Return a simple analysis snapshot of the agent."""
        return {
            "state": self.agent.state,
            "tension": self.agent.tension,
            "emotion": self.agent.emotion,
        }

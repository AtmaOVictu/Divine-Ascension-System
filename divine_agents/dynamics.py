"""Utility classes dealing with emotional and tension adjustments."""

from .agent import Agent


class EmotionalTensionDynamics:
    """Adjust an agent's tension based on its emotional label."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def adjust_tension(self) -> None:
        """Modify tension depending on the agent's emotional label."""
        emotion = getattr(self.agent, "emotion_label", "neutral")
        if emotion == "angry":
            self.agent.tension += 0.3
        elif emotion == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1

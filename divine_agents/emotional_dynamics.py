from __future__ import annotations

from .advanced_agent import MultiLayeredAgent


class EmotionalTensionDynamics:
    """Adjust an agent's tension based on qualitative emotions."""

    def __init__(self, agent: MultiLayeredAgent) -> None:
        self.agent = agent

    def adjust_tension(self) -> None:
        """Change tension based on the agent's emotion label."""
        label = getattr(self.agent, "emotion_label", "neutral")
        if label == "angry":
            self.agent.tension += 0.3
        elif label == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1

"""Utilities for verifying and analysing agent transitions."""

from .agent import Agent


class TransitionVerifier:
    """Helper class for checking and dissecting agent state transitions."""

    def __init__(self, agent: Agent, transition_threshold: float = 0.7, emotion_threshold: float = 0.5):
        self.agent = agent
        self.transition_threshold = transition_threshold
        self.emotion_threshold = emotion_threshold

    def verify_transition(self) -> str:
        """Trigger a transition when thresholds are met and return the new state."""
        if self.agent.tension > self.transition_threshold or self.agent.emotion > self.emotion_threshold:
            return self.agent.transition()
        return self.agent.state

    def seciraj(self) -> str:
        """Provide analysis of the agent's current phase."""
        if self.agent.state in ["Jaz", "Enotnost"]:
            return self.agent.analyze_phase()
        return self.agent.hold_state()

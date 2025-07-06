"""Decision-making logic for agent state transitions."""

from __future__ import annotations


class DecisionMaker:
    """Determine state transitions based on an agent's tension and emotion."""

    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, agent: "Agent") -> None:
        self.agent = agent

    def decide_transition(self) -> str:
        """Return the next state for the associated agent."""
        if self.agent.tension > self.TENSION_THRESHOLD or self.agent.emotion > self.EMOTION_THRESHOLD:
            if self.agent.state == "Ego":
                return "Jaz"
            if self.agent.state == "Jaz":
                return "Enotnost"
        return self.agent.state

from __future__ import annotations

from .agent import Agent


class DecisionMaker:
    """Determine state transitions for an agent based on tension, emotion and history."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def decide_transition(self) -> str:
        """Decide and apply the next state for the associated agent."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz":
                self.agent.state = "Enotnost"
        else:
            recent = self.agent.history[-3:]
            if self.agent.state == "Ego" and recent.count("Ego") == len(recent):
                self.agent.state = "Jaz"
        self.agent.history.append(self.agent.state)
        return self.agent.state

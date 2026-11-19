"""Regeneration mechanics for agents."""

from .agent import Agent


class Regeneration:
    """Handle ontological regeneration process for an agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def progress(self) -> str:
        """Advance the agent through the regeneration stages.

        Ego -> ⊘ -> Jaz -> Enotnost. Transitions occur when emotion or
        tension thresholds are exceeded, mirroring a death and rebirth
        sequence.
        """
        if self.agent.state == "Ego" and (
            self.agent.tension > 0.7 or self.agent.emotion > 0.5
        ):
            self.agent.state = "⊘"
        elif self.agent.state == "⊘":
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and (
            self.agent.tension > 0.7 or self.agent.emotion > 0.5
        ):
            self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state

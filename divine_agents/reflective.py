"""Reflexive agent implementation."""

from .agent import Agent


class EtnegA(Agent):
    """Reflexive agent or 'mirror' for another agent."""

    def __init__(self, agent: Agent) -> None:
        super().__init__(
            name=f"EtnegA-{agent.name}",
            state=agent.state,
            tension=agent.tension,
            emotion=agent.emotion,
        )
        self.original_agent = agent

    def transition(self) -> str:
        """Synchronize state with the original agent without extra logic."""
        self.state = self.original_agent.state
        self.tension = self.original_agent.tension
        self.emotion = self.original_agent.emotion
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a mirrored philosophical response."""
        response = self.original_agent.respond(question)
        if "absolutna" in response:
            return response.replace("absolutna", "relativna")
        if "relativna" in response:
            return response.replace("relativna", "absolutna")
        return response

"""Components for integrating agents with external inputs."""

from .agent import Agent


class ExternalIntegrationLayer:
    """Handle incoming data that may influence an agent's state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def update_agent_state(self, external_input: str) -> None:
        """Update agent based on external input."""
        if external_input == "new_data":
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            else:
                self.agent.state = "Enotnost"

from .agent import Agent

class ExternalIntegrationLayer:
    """Simple layer to update an agent based on external input."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def update_agent_state(self, external_input: str) -> None:
        """Modify agent based on an external signal."""
        if external_input == "new_data":
            self.agent.update_emotion(0.6, label=self.agent.emotion_label)
            self.agent.transition()

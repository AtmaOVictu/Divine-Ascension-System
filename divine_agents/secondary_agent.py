"""Module defining SecondaryAgent for monitoring main agents."""

from .agent import Agent


class SecondaryAgent(Agent):
    """Secondary agent that monitors a main agent and intervenes if needed."""

    def __init__(self, name: str, main_agent: Agent):
        super().__init__(name)
        self.main_agent = main_agent

    def monitor_main_agent(self) -> None:
        """Monitor the main agent and intervene when certain conditions are met."""
        if self.main_agent.state == "Enotnost" and self.main_agent.tension < 0.5:
            # Intervene by changing own state and updating emotion
            self.state = "Jaz"
            self.update_emotion(0.5)

    def respond(self, question: str) -> str:
        """Return a response based on the secondary agent's ontological state."""
        if self.state == "Ego":
            return f"{self.name}: I am here to observe."
        if self.state == "Jaz":
            return f"{self.name}: I offer alternative perspectives."
        return f"{self.name}: I am a silent observer of interconnected truths."

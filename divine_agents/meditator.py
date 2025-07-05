class Meditator:
    """Facilitate self-reflection and peaceful transitions for an agent."""

    def __init__(self, agent):
        self.agent = agent

    def self_reflection(self) -> str:
        """Return the agent's current emotional overview."""
        return (
            f"Trenutno stanje: {self.agent.state}; "
            f"Napetost: {self.agent.tension}, Čustva: {self.agent.emotion}"
        )

    def transition_to_peace(self) -> str:
        """Move the agent to a harmonious state if conditions are met."""
        if self.agent.tension < 0.3:
            self.agent.state = "Enotnost"
            return "Agent prehaja v stanje Enotnost."
        return "Prehodi so potrebni, da dosežeš notranje ravnovesje."

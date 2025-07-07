class LogarithmOfReason:
    """Provide reasoning for an agent's potential transition."""

    def __init__(self, agent):
        self.agent = agent

    def calculate_reason(self) -> str:
        """Calculate and return a textual explanation for the agent's transition."""
        reason_value = self.agent.tension * self.agent.emotion
        if reason_value > 0.5:
            return "Prehod je nujen, vendar premislimo o posledicah."
        if reason_value > 0.3:
            return "Prehod ni nujen, vendar raziskujmo možnost."
        return "Prehod je nepotreben, zadržimo se v trenutnem stanju."

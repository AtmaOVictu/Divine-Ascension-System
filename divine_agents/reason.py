class LogarithmOfReason:
    """Calculate reasons for an agent's state transitions."""

    def __init__(self, agent):
        self.agent = agent

    def calculate_reason(self) -> str:
        """Return textual reasoning for the agent's potential transition."""
        reason_value = self.agent.tension * self.agent.emotion
        if reason_value > 0.5:
            return "Prehod je nujen, vendar premislimo o posledicah."
        elif reason_value > 0.3:
            return "Prehod ni nujen, vendar raziskujmo možnost."
        return "Prehod je nepotreben, zadržimo se v trenutnem stanju."

class UcenjeIzIzkusenj:
    """Simple rule-based learning from past actions."""

    def __init__(self, agent):
        self.agent = agent

    def odlocitev(self, situacija: str) -> str:
        """Return decision based on history."""
        if situacija == "danger":
            if "helped" in self.agent.history:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"

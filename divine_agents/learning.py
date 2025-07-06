class UcenjeIzIzkusenj:
    """Simple mechanism for adapting decisions based on history."""

    def __init__(self, agent):
        self.agent = agent
        self.history = agent.history

    def uci_se(self, situacija: str) -> str:
        """Learn from previous experiences to adapt future decisions."""
        if situacija == "danger":
            if "helped" in self.history:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"

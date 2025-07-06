class HistoricalRefactor:
    """Analyse agent history to suggest adjustments."""

    def __init__(self, agent):
        self.agent = agent

    def auto_refactor(self) -> str:
        if "hesitation" in self.agent.history[-3:]:
            return "Prehod v Jaz zaradi negotovosti."
        if "self-preservation" in self.agent.experiences:
            return "Agent ostaja v Egu zaradi sebičnosti."
        return "Stanje je stabilno, prehod ni potreben."

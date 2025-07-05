class EthicsJudgement:
    """Simple ethical evaluation of agent decisions."""

    def __init__(self):
        self.last_judgement = "Neutral"

    def evaluate(self, decision: str) -> str:
        """Return an ethical judgement for a decision."""
        if decision.lower() == "egoizem":
            self.last_judgement = "Unethical"
        else:
            self.last_judgement = "Ethical"
        return self.last_judgement

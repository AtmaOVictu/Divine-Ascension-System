class EthicalJudge:
    """Simple ethical evaluation for agent decisions."""

    def judge(self, decision: str) -> str:
        if decision.lower() == "egoizem":
            return "Neetično"
        return "Etično"

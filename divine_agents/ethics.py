class EthicalAssessment:
    """Assess ethical decisions."""

    def __init__(self):
        self.status = "Nevtralno"

    def assess(self, decision: str) -> str:
        """Return ethical evaluation of a decision."""
        if decision == "egoizem":
            self.status = "Neetično"
        else:
            self.status = "Etično"
        return self.status

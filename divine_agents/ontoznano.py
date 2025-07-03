class Ontoznano:
    """Tracks an agent's progression through ontological phases."""

    def __init__(self):
        self.area = "neznano"
        self.progress = 0
        self.history = []

    def transition(self, stage: str) -> str:
        """Update the current ontological stage."""
        if stage == "samospoznanje":
            self.area = "poznavanje lastne resnice"
            self.progress = 100
        elif stage == "logični prehod":
            self.area = "logična analiza"
            self.progress = 50
        elif stage == "emotivni prehod":
            self.area = "emocionalna refleksija"
            self.progress = 75
        else:
            self.area = "neznano"
            self.progress = 0
        self.history.append((stage, self.progress))
        return self.area

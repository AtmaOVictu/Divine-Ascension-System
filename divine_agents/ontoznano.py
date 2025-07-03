class Ontoznano:
    """Track agent progression through ontological phases."""

    def __init__(self):
        self.area = "neznano"
        self.progress = 0
        self.history = []

    def transition(self, phase: str) -> str:
        """Move agent into a new philosophical phase."""
        if phase == "samospoznanje":
            self.area = "poznavanje lastne resnice"
            self.progress = 100
        elif phase == "logični prehod":
            self.area = "logična analiza"
            self.progress = 50
        elif phase == "emotivni prehod":
            self.area = "emocionalna refleksija"
            self.progress = 75
        else:
            self.area = "neznano"
            self.progress = 0
        self.history.append((phase, self.progress))
        return self.area

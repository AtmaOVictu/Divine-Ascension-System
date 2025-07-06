class Memory:
    """Simple memory store for agent experiences."""

    def __init__(self):
        self.log = []

    def remember(self, entry: str) -> None:
        self.log.append(entry)

    def recall_last(self) -> str:
        return self.log[-1] if self.log else ""

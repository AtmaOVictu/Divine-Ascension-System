class SimpleRL:
    """Minimal reinforcement learning stub."""

    def __init__(self):
        self.reward = 0

    def update(self, value: float) -> None:
        self.reward += value

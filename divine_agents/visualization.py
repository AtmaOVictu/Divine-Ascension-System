class TransitionVisualizer:
    """Record and visualize agent state transitions."""

    def __init__(self):
        self.history = []

    def record(self, state: str) -> None:
        self.history.append(state)

    def ascii_path(self) -> str:
        return " -> ".join(self.history)

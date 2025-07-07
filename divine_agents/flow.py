class Flow:
    """Represents a flow of states for an agent."""
    def __init__(self, name: str, initial_state: str = "Ego"):
        self.name = name
        self.history = [initial_state]

    def update(self, state: str) -> None:
        self.history.append(state)

    @property
    def current(self) -> str:
        return self.history[-1]

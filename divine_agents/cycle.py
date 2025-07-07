class RecursiveBox:
    """A box representing a task where 0 is both the end and the beginning."""

    def __init__(self, name: str, state: int = 0, data: dict | None = None):
        self.name = name
        self.state = state
        self.data = data if data else {"status": "initialized"}
        self.history = [state]

    def transition(self, next_state: int, new_data: dict):
        if next_state not in (0, 1):
            raise ValueError("State must be either 0 or 1")
        self.history.append(next_state)
        self.state = next_state
        self.data.update(new_data)
        if self.state == 0:
            return f"Box '{self.name}' has completed its cycle and reset to 0."
        return f"Box '{self.name}' is now in active state (1)."

    def unpack(self) -> dict:
        return self.data

    def __str__(self) -> str:
        return f"Box '{self.name}' with state {self.state} and data: {self.data}"

class StateBox:
    """A box holding a state (0 or 1) and associated data."""

    def __init__(self, state: int, data: dict | None = None):
        if state not in (0, 1):
            raise ValueError("State must be 0 or 1")
        self.state = state
        self.data = data.copy() if data else {"status": "initialized"}
        self.history = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update data inside the box while preserving history."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Set or unset modification protection."""
        self.protection_flag = flag

    def transition(self, next_state: int, new_data: dict | None = None) -> int:
        """Transition to the next valid state and update the data."""
        if next_state not in (0, 1):
            raise ValueError("State transition is invalid. Only 0 and 1 are allowed.")
        if new_data:
            self.update_data(new_data)
        self.state = next_state
        return self.state

    def unpack(self) -> dict:
        """Return the current data without modifying state."""
        return self.data

    def __str__(self) -> str:
        return f"Box with state {self.state} and data: {self.data}"

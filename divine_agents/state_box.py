class StateBox:
    """A box that encapsulates a state (0 or 1) and associated data."""

    def __init__(self, state: int, data: dict | None = None):
        if state not in (0, 1):
            raise ValueError("State must be 0 or 1")
        self.state = state
        self.data = data if data is not None else {"status": "initialized"}
        self.history = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the internal data while preserving history."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Enable or disable protection against updates."""
        self.protection_flag = flag

    def transition(self, next_state: int, new_data: dict) -> None:
        """Move to the next state if valid and apply new data."""
        if next_state not in (0, 1):
            raise ValueError("State transition is invalid. Only 0 and 1 are allowed.")
        self.update_data(new_data)
        self.state = next_state

    def unpack(self) -> dict:
        """Return the current data for inspection."""
        return self.data

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Box with state {self.state} and data: {self.data}"

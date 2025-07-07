class BoxWithZero:
    """A box that always contains 0 as its starting point."""
    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        # ensure the state key exists and defaults to 0
        self.data = data.copy() if data else {}
        self.data.setdefault("state", 0)
        self.history: list[dict] = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box data while keeping state 0 unless changed explicitly."""
        if self.protection_flag:
            raise PermissionError(f"{self.name} box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)
        self.data.setdefault("state", 0)

    def set_protection(self, flag: bool) -> None:
        """Enable or disable modification protection."""
        self.protection_flag = flag

    def transition(self, next_state: str, new_data: dict | None = None) -> None:
        """Transition to the next state while updating data."""
        if new_data:
            self.update_data(new_data)
        self.data["state"] = next_state

    def unpack(self) -> dict:
        """Return the current box contents."""
        return self.data

    def __str__(self) -> str:
        return f"Box '{self.name}' with data: {self.data}"

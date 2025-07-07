class IntegrityBox:
    """A box that tracks the integrity of an entity and its state."""

    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        self.data = data.copy() if data else {"integrity_status": "valid"}
        self.history = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box's data, storing the previous state in history."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Enable or disable modification protection."""
        self.protection_flag = flag

    def transition(self, new_data: dict) -> None:
        """Transition to a new state and store the previous one."""
        self.update_data(new_data)

    def check_integrity(self) -> str:
        """Return the current integrity status."""
        return self.data.get("integrity_status", "unknown")

    def __repr__(self) -> str:  # pragma: no cover - debug purpose
        return f"IntegrityBox(name={self.name}, data={self.data}, protected={self.protection_flag})"

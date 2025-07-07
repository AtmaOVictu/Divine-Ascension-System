class IntegrityBox:
    """A box that holds and tracks the integrity of an entity or task."""

    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        self.data = data if data is not None else {"integrity_status": "valid"}
        self.history = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update data while preserving history."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Set or unset the protection flag."""
        self.protection_flag = flag

    def transition(self, new_data: dict) -> None:
        """Transition to a new state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.update_data(new_data)

    def check_integrity(self) -> str:
        """Return the current integrity status."""
        return self.data.get("integrity_status", "unknown")

    def __str__(self) -> str:
        return f"Box for {self.name} with data: {self.data} and protection: {self.protection_flag}"

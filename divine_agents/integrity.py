class IntegrityBox:
    """Container that tracks the integrity and history of an entity."""
    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        self.data = data.copy() if data else {"integrity_status": "valid"}
        self.history: list[dict] = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the contained data and store previous state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def transition(self, new_data: dict) -> None:
        """Transition to a new state by updating data."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.update_data(new_data)

    def set_protection(self, flag: bool) -> None:
        self.protection_flag = flag

    def check_integrity(self) -> str:
        return self.data.get("integrity_status", "unknown")

    def __str__(self) -> str:
        return f"Box for {self.name} with data: {self.data}"

class ExtraSymbolicBox:
    """An extra symbolic box to act as fallback and validation layer."""

    def __init__(self, stage: str = "∴", data: dict | None = None):
        self.stage = stage
        self.data = data or {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update box data unless protected."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Toggle modification protection."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict | None = None) -> None:
        """Move the box to the next stage, updating data."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.stage = next_stage
        if new_data:
            self.update_data(new_data)

    def get_data(self) -> dict:
        """Return stored data."""
        return self.data

    def __str__(self) -> str:
        return f"Extra Box at {self.stage} stage with data: {self.data}"

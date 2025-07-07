class SymbolicBox:
    """A symbolic container for task or data with built-in protections."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data or {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the data inside the box if protection allows."""
        if self.protection_flag:
            raise PermissionError("Cannot modify data, the box is protected.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Enable or disable protection on the box."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict | None = None) -> None:
        """Move to the next stage and optionally update data."""
        if self.protection_flag:
            raise PermissionError("Cannot transition, the box is protected.")
        self.stage = next_stage
        if new_data:
            self.update_data(new_data)

    def get_data(self) -> dict:
        """Retrieve the current stored data."""
        return self.data

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"

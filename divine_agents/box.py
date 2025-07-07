class SymbolicBox:
    """Represents an ontological stage container."""

    def __init__(self, stage: str, data: dict | None = None):
        if not data:
            raise ValueError("Data cannot be empty. Boxes are necessary for task processing.")
        self.stage = stage
        self.data = data

    def update_data(self, new_data: dict) -> None:
        """Update stored data with new values."""
        self.data.update(new_data)

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Move to the next ontological stage and update data."""
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        """Retrieve current data."""
        return self.data

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"

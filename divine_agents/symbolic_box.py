class SymbolicBox:
    """Represents an ontological stage packaged in a symbolic box."""

    def __init__(self, stage: str, data: dict):
        if not data:
            raise ValueError("Data cannot be empty. Boxes are necessary for task processing.")
        self.stage = stage
        self.data = data

    def update_data(self, new_data: dict) -> None:
        """Update the box with new data."""
        self.data.update(new_data)

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Move the box to the next ontological stage."""
        self.stage = next_stage
        self.update_data(new_data)

    def __repr__(self) -> str:
        return f"SymbolicBox(stage={self.stage}, data={self.data})"

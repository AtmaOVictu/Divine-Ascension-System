class SymbolicBox:
    """Represents an ontological task box with error handling."""

    VALID_STAGES = ["∴", "∆", "⊘"]

    def __init__(self, stage: str, data: dict):
        if not data:
            raise ValueError("Data cannot be empty. Boxes are necessary for task processing.")
        if stage not in self.VALID_STAGES:
            raise ValueError(f"Invalid stage {stage}. Expected one of {', '.join(self.VALID_STAGES)}.")
        self.stage = stage
        self.data = data.copy()

    def update_data(self, new_data: dict) -> None:
        """Update the box with new data during ontological transformations."""
        self.data.update(new_data)

    def transition(self, next_stage: str, new_data: dict = None) -> None:
        """Move to the next ontological stage if valid."""
        if next_stage not in self.VALID_STAGES:
            raise ValueError(f"Invalid transition to {next_stage}. Only {', '.join(self.VALID_STAGES)} are valid.")
        self.stage = next_stage
        if new_data:
            self.update_data(new_data)

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"

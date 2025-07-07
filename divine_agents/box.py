class RecursiveSymbolicBox:
    """A recursive symbolic box for ontological transitions."""

    def __init__(self, stage: str, data: dict | None = None):
        if not data:
            raise ValueError("Data cannot be empty. Boxes are necessary for task processing.")
        self.stage = stage
        self.data = data
        self.previous_state: tuple[str, dict] | None = None

    def update_data(self, new_data: dict) -> None:
        """Update the box with new data during transformations."""
        self.data.update(new_data)

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Move to the next ontological stage, keeping track of previous state."""
        self.previous_state = (self.stage, self.data.copy())
        self.stage = next_stage
        self.update_data(new_data)

    def rollback(self) -> None:
        """Roll back to the previous state if it exists."""
        if not self.previous_state:
            raise RuntimeError("No previous state to roll back to.")
        self.stage, self.data = self.previous_state
        self.previous_state = None

    def get_data(self) -> dict:
        """Return current data."""
        return self.data

    def __str__(self) -> str:  # pragma: no cover - simple utility
        return f"Box at {self.stage} stage with data: {self.data}"

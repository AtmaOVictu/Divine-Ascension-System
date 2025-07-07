class SymbolicBox:
    """Container for ontological data at different stages."""
    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data or {}

    def update_data(self, new_data: dict) -> None:
        self.data.update(new_data)

    def get_data(self) -> dict:
        return self.data

    def __str__(self) -> str:
        return f"Box at {self.stage} with data: {self.data}"


def initiate_task(task_name: str) -> SymbolicBox:
    """Create a box representing the start of a task."""
    return SymbolicBox(stage="∴", data={"task_name": task_name, "status": "initiated"})


def process_task(box: SymbolicBox, updates: dict) -> SymbolicBox:
    """Update the box with intermediate data and mark transformation."""
    box.update_data(updates)
    box.stage = "∆"
    return box


def resolve_task(box: SymbolicBox) -> SymbolicBox:
    """Mark the task as completed and close the box."""
    box.stage = "⊘"
    box.update_data({"status": "completed"})
    return box

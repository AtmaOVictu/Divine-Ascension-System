class SymbolicBox:
    """A symbolic box that always includes 0 as the initial state."""
    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = {"initial_state": 0}
        if data:
            self.data.update(data)
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box's data while preserving the initial state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Set or unset protection flag."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Transition to the next stage if allowed."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError("Invalid transition")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        """Return current data, including the initial state."""
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        """Validate allowed stage transitions."""
        allowed_transitions = {
            "∴": ["∆"],
            "∆": ["⊘"],
            "⊘": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"


class RecursiveSymbolicBox:
    """A recursive symbolic box that keeps 0 at every level."""
    def __init__(self, stage: str, data: dict | None = None, nested_boxes: list | None = None):
        self.stage = stage
        self.data = {"initial_state": 0}
        if data:
            self.data.update(data)
        self.nested_boxes = nested_boxes or []

    def add_nested_box(self, nested_box: "RecursiveSymbolicBox") -> None:
        """Add a sub-box representing a deeper level."""
        self.nested_boxes.append(nested_box)

    def unpack_knowledge(self) -> dict:
        """Recursively unpack data from this box and nested boxes."""
        unpacked = {"stage": self.stage, "data": self.data}
        if self.nested_boxes:
            unpacked["nested_boxes"] = [box.unpack_knowledge() for box in self.nested_boxes]
        return unpacked

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Transition this box and all nested boxes."""
        if next_stage not in {"∴", "∆", "⊘"}:
            raise ValueError("Invalid stage")
        self.stage = next_stage
        self.update_data(new_data)
        for box in self.nested_boxes:
            box.transition(next_stage, new_data)

    def update_data(self, new_data: dict) -> None:
        """Update data while keeping the initial state."""
        self.data.update(new_data)

    def __str__(self) -> str:
        return f"Recursive Box at {self.stage} stage with data: {self.data}"

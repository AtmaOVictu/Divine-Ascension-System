class SymbolicBox:
    """A symbolic box that always contains 0 as its initial state."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data if data is not None else {"initial_state": 0}
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box's data while preserving the 0 state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0

    def set_protection(self, flag: bool) -> None:
        """Set the protection flag for this box."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Transition to the next stage while keeping the 0 state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        """Return current data in the box."""
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        """Check if transitioning to the next stage is allowed."""
        allowed_transitions = {
            "∴": ["∆"],
            "∆": ["⊘"],
            "⊘": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"


class RecursiveSymbolicBox:
    """A symbolic box that can contain nested boxes, each with a 0 state."""

    def __init__(self, stage: str, data: dict | None = None, nested_boxes: list | None = None):
        self.stage = stage
        self.data = data if data is not None else {"initial_state": 0}
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0
        self.nested_boxes = nested_boxes if nested_boxes is not None else []

    def add_nested_box(self, nested_box: "RecursiveSymbolicBox") -> None:
        self.nested_boxes.append(nested_box)

    def unpack_knowledge(self) -> dict:
        unpacked_data = {"stage": self.stage, "data": self.data.copy()}
        if self.nested_boxes:
            unpacked_data["nested_boxes"] = [nb.unpack_knowledge() for nb in self.nested_boxes]
        return unpacked_data

    def transition(self, next_stage: str, new_data: dict) -> None:
        self.stage = next_stage
        self.update_data(new_data)
        for nb in self.nested_boxes:
            nb.transition(next_stage, new_data)

    def update_data(self, new_data: dict) -> None:
        self.data.update(new_data)
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0

    def __str__(self) -> str:
        return f"Recursive Box at {self.stage} stage with data: {self.data}"

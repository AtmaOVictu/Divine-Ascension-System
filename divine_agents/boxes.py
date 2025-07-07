class SymbolicBox:
    """A symbolic box that always contains 0 as its initial state."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = {"initial_state": 0}
        if data:
            self.data.update(data)
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box's data while preserving the 0 state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Set or unset box protection."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Move to the next stage, maintaining the 0 state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        """Return the data currently stored in the box."""
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        """Validate that the next stage is allowed from the current one."""
        allowed_transitions = {
            "∴": ["∆"],
            "∆": ["⊘"],
            "⊘": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"


class RecursiveSymbolicBox(SymbolicBox):
    """A symbolic box that can contain nested boxes."""

    def __init__(self, stage: str, data: dict | None = None, nested_boxes: list | None = None):
        super().__init__(stage, data)
        self.nested_boxes = nested_boxes if nested_boxes else []

    def add_nested_box(self, nested_box: 'RecursiveSymbolicBox') -> None:
        """Add a nested box."""
        self.nested_boxes.append(nested_box)

    def unpack_knowledge(self) -> dict:
        """Recursively unpack all nested boxes into dictionaries."""
        unpacked = {"stage": self.stage, "data": self.data, "nested_boxes": []}
        for box in self.nested_boxes:
            unpacked["nested_boxes"].append(box.unpack_knowledge())
        return unpacked

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Transition this box and all nested boxes."""
        super().transition(next_stage, new_data)
        for box in self.nested_boxes:
            box.transition(next_stage, new_data)


"""Symbolic containers used for representing ontological knowledge.

These boxes always include a foundational state ``0`` in their data. The
classes allow transitions between symbolic stages while preserving the
initial state. They can also contain nested boxes for recursive
structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SymbolicBox:
    """A symbolic box that always contains ``0`` as the initial state."""

    stage: str
    data: Dict[str, object] = field(default_factory=dict)
    protection_flag: bool = False

    def __post_init__(self) -> None:
        # Ensure the box always starts with an ``initial_state`` of 0
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0

    def update_data(self, new_data: Dict[str, object]) -> None:
        """Update the box's data while preserving the ``0`` state."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)
        if "initial_state" not in self.data:
            self.data["initial_state"] = 0

    def set_protection(self, flag: bool) -> None:
        """Enable or disable protection for the box."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: Dict[str, object]) -> None:
        """Move to the next stage if modifications are allowed."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError(f"Invalid transition from {self.stage} to {next_stage}")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> Dict[str, object]:
        """Return the current data including the ``0`` state."""
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        """Return ``True`` if the transition is allowed."""
        allowed_transitions = {
            "∴": ["∆"],
            "∆": ["⊘"],
            "⊘": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at {self.stage} stage with data: {self.data}"


@dataclass
class RecursiveSymbolicBox(SymbolicBox):
    """A box that can contain nested ``SymbolicBox`` instances."""

    nested_boxes: List[SymbolicBox] = field(default_factory=list)

    def add_nested_box(self, nested_box: SymbolicBox) -> None:
        """Add a nested box representing a sub-task or phase."""
        self.nested_boxes.append(nested_box)

    def unpack_knowledge(self) -> Dict[str, object]:
        """Recursively unpack knowledge contained within nested boxes."""
        unpacked = {"stage": self.stage, "data": self.data, "nested_boxes": []}
        for box in self.nested_boxes:
            unpacked["nested_boxes"].append(box.unpack_knowledge() if isinstance(box, RecursiveSymbolicBox) else {"stage": box.stage, "data": box.data})
        return unpacked

    def transition(self, next_stage: str, new_data: Dict[str, object]) -> None:
        """Transition self and all nested boxes to the next stage."""
        super().transition(next_stage, new_data)
        for box in self.nested_boxes:
            box.transition(next_stage, new_data)

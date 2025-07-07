"""Symbolic box for ontological task management."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


VALID_STAGES = ("∴", "∆", "⊘")


@dataclass
class SymbolicBox:
    """Container enforcing ontological flow with built-in error handling."""

    stage: str
    data: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.data:
            raise ValueError(
                "Data cannot be empty. Boxes are necessary for task processing."
            )
        if self.stage not in VALID_STAGES:
            raise ValueError(
                f"Invalid stage {self.stage}. Expected one of {', '.join(VALID_STAGES)}."
            )

    def update_data(self, new_data: Dict[str, str]) -> None:
        """Update the box with new data during ontological transformations."""
        self.data.update(new_data)

    def get_data(self) -> Dict[str, str]:
        """Retrieve data from the box."""
        return self.data

    def transition(self, next_stage: str, new_data: Dict[str, str]) -> None:
        """Move to the next ontological stage if valid."""
        if next_stage not in VALID_STAGES:
            raise ValueError(
                f"Invalid transition to {next_stage}. Only {', '.join(VALID_STAGES)} are valid."
            )
        self.stage = next_stage
        self.update_data(new_data)

    def __str__(self) -> str:  # pragma: no cover - debug helper
        return f"Box at {self.stage} stage with data: {self.data}"


def initiate_task_with_box(task_name: str) -> SymbolicBox:
    """Initialize task and create symbolic box (∴)."""
    return SymbolicBox(stage="∴", data={"task_name": task_name, "status": "initiated"})


def process_task_with_box(symbolic_box: SymbolicBox, input_data: str) -> SymbolicBox:
    """Process the task in a symbolic box (∆)."""
    if symbolic_box.stage != "∴":
        raise ValueError("Task must be initiated (∴) before processing (∆).")
    symbolic_box.transition("∆", {"processed_data": f"{input_data} processed."})
    return symbolic_box


def resolve_task_with_box(symbolic_box: SymbolicBox) -> SymbolicBox:
    """Resolve the task and complete the box (⊘)."""
    if symbolic_box.stage != "∆":
        raise ValueError("Task must be processed (∆) before resolving (⊘).")
    symbolic_box.transition("⊘", {"status": "completed"})
    return symbolic_box

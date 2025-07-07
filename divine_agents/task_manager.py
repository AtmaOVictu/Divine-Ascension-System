from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class TaskManager:
    """Manage open and closed branches in the system."""

    open_branches: List[str] = field(default_factory=list)
    closed_branches: List[str] = field(default_factory=list)
    points: int = 0

    def add_open_branch(self, branch: str) -> None:
        """Register a new open branch."""
        if branch not in self.open_branches:
            self.open_branches.append(branch)

    def close_branch(self, branch: str) -> None:
        """Close an existing branch and update scoring."""
        if branch in self.open_branches:
            self.open_branches.remove(branch)
            self.closed_branches.append(branch)
            self.points += 1
            self.check_for_progress()

    def check_for_progress(self) -> None:
        """Advance when all branches are closed."""
        if not self.open_branches:
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Placeholder for progressing to the next stage."""
        # In a full system this might trigger new tasks or events.
        self.points = 0

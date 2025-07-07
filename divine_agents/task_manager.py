import uuid
from typing import Dict, List


class TaskManager:
    """Manage branches (tasks) with unique IDs and history."""

    def __init__(self) -> None:
        self.open_branches: Dict[uuid.UUID, Dict[str, str]] = {}
        self.history: List[Dict[str, str]] = []

    def add_open_branch(self, branch_name: str) -> uuid.UUID:
        """Add a new open branch with a unique ID."""
        branch_id = uuid.uuid4()
        self.open_branches[branch_id] = {"name": branch_name, "status": "open"}
        return branch_id

    def close_branch(self, branch_id: uuid.UUID) -> None:
        """Close a branch based on ID and log it to history."""
        branch = self.open_branches.get(branch_id)
        if branch:
            branch["status"] = "closed"
            self.history.append(branch)
            self.check_for_progress()

    def check_for_progress(self) -> None:
        """Check if all branches are closed and advance stage."""
        if self.open_branches and all(b["status"] == "closed" for b in self.open_branches.values()):
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Advance to the next stage and clear history."""
        self.history.clear()

    def find_related_branches(self, branch_id: uuid.UUID) -> List[uuid.UUID]:
        """Find branches with the same name."""
        target = self.open_branches.get(branch_id)
        if not target:
            return []
        return [bid for bid, b in self.open_branches.items() if b["name"] == target["name"] and bid != branch_id]

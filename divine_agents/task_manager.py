import uuid
from typing import Dict, List


class TaskManager:
    """Manage branches (tasks) with unique IDs and track their progress."""

    def __init__(self) -> None:
        self.open_branches: Dict[uuid.UUID, Dict[str, str]] = {}
        self.history: List[Dict[str, str]] = []

    def add_open_branch(self, branch_name: str) -> uuid.UUID:
        """Add a new open branch with a unique ID."""
        branch_id = uuid.uuid4()
        self.open_branches[branch_id] = {"name": branch_name, "status": "open"}
        return branch_id

    def close_branch(self, branch_id: uuid.UUID) -> None:
        """Close a branch based on its ID and record it in history."""
        branch = self.open_branches.get(branch_id)
        if branch:
            branch["status"] = "closed"
            self.history.append(branch)
            self.check_for_progress()
        else:
            raise KeyError(f"No branch with ID {branch_id}")

    def check_for_progress(self) -> None:
        """If all branches are closed, prepare to advance."""
        if self.open_branches and all(b["status"] == "closed" for b in self.open_branches.values()):
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Clear history to represent advancing to the next stage."""
        self.history.clear()

    def find_related_branches(self, branch_id: uuid.UUID) -> List[uuid.UUID]:
        """Find branches with the same name as the given branch ID."""
        if branch_id not in self.open_branches:
            raise KeyError(f"No branch with ID {branch_id}")
        target_name = self.open_branches[branch_id]["name"]
        return [bid for bid, branch in self.open_branches.items() if branch["name"] == target_name and bid != branch_id]

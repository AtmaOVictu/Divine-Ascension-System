import uuid
from typing import Dict, List


class TaskManager:
    """Manage branches (tasks) using unique identifiers."""

    def __init__(self) -> None:
        self.open_branches: Dict[uuid.UUID, Dict[str, str]] = {}
        self.history: List[Dict[str, str]] = []

    def add_open_branch(self, branch_name: str) -> uuid.UUID:
        """Add a new open branch with a unique ID."""
        branch_id = uuid.uuid4()
        self.open_branches[branch_id] = {"name": branch_name, "status": "open"}
        return branch_id

    def close_branch(self, branch_id: uuid.UUID) -> None:
        """Close a branch by ID and record it in history."""
        if branch_id in self.open_branches:
            self.open_branches[branch_id]["status"] = "closed"
            self.history.append(self.open_branches[branch_id])
            self.check_for_progress()
        else:
            raise KeyError(f"Branch with ID {branch_id} not found")

    def check_for_progress(self) -> None:
        """Advance to next stage if all branches are closed."""
        if all(branch["status"] == "closed" for branch in self.open_branches.values()):
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Simulate advancing to the next phase."""
        self.history.clear()

    def find_related_branches(self, branch_id: uuid.UUID) -> List[uuid.UUID]:
        """Find branches with the same name as the given branch."""
        if branch_id not in self.open_branches:
            return []
        name = self.open_branches[branch_id]["name"]
        return [bid for bid, info in self.open_branches.items() if info["name"] == name and bid != branch_id]

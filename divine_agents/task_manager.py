import uuid
from typing import Dict, List, Optional


class TaskManager:
    """Manage tasks (kraki) identified by unique IDs."""

    def __init__(self) -> None:
        self.open_branches: Dict[uuid.UUID, Dict[str, str]] = {}
        self.history: List[Dict[str, str]] = []

    def add_open_branch(self, branch_name: str) -> uuid.UUID:
        """Add a new open branch with a unique ID."""
        branch_id = uuid.uuid4()
        self.open_branches[branch_id] = {"name": branch_name, "status": "open"}
        return branch_id

    def close_branch(self, branch_id: uuid.UUID) -> bool:
        """Close a branch by ID and store it in history."""
        branch = self.open_branches.get(branch_id)
        if branch:
            branch["status"] = "closed"
            self.history.append(branch)
            return True
        return False

    def check_for_progress(self) -> bool:
        """Return True if all branches are closed."""
        if self.open_branches and all(b["status"] == "closed" for b in self.open_branches.values()):
            self.history.clear()
            return True
        return False

    def find_related_branches(self, branch_id: uuid.UUID) -> List[uuid.UUID]:
        """Find branches with the same name as the provided ID."""
        related: List[uuid.UUID] = []
        branch = self.open_branches.get(branch_id)
        if not branch:
            return related
        for b_id, data in self.open_branches.items():
            if b_id != branch_id and data["name"] == branch["name"]:
                related.append(b_id)
        return related

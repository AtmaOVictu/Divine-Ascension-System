class TaskManager:
    """Manage open and closed branches with progress tracking."""

    def __init__(self):
        self.open_branches = []
        self.closed_branches = []
        self.points = 0
        self.stage = 0

    def add_open_branch(self, branch: str) -> None:
        """Add a new branch to the open list."""
        if branch not in self.open_branches:
            self.open_branches.append(branch)

    def close_branch(self, branch: str) -> None:
        """Close a branch and update progress."""
        if branch in self.open_branches:
            self.open_branches.remove(branch)
            self.closed_branches.append(branch)
            self.points += 1
            self.check_for_progress()

    def check_for_progress(self) -> None:
        """Advance stage if all branches are closed."""
        if not self.open_branches:
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Move to the next stage and reset points."""
        self.stage += 1
        self.points = 0

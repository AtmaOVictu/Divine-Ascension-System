class TaskManager:
    """Manage open and closed branches (kraki) with history."""

    def __init__(self):
        self.history = []
        self.open_branches = []
        self.closed_branches = []

    def add_open_branch(self, branch: str) -> None:
        """Add a new open branch."""
        self.open_branches.append(branch)

    def close_branch(self, branch: str) -> None:
        """Close a branch and record progress."""
        if branch in self.open_branches:
            self.open_branches.remove(branch)
            self.closed_branches.append(branch)
            self.history.append(f"Krake {branch} zaključen.")
            self.check_for_progress()

    def check_for_progress(self) -> None:
        """Advance if all branches are closed."""
        if not self.open_branches:
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Open new branches based on history."""
        if "Krake A zaključen." in self.history:
            self.open_branches.append("Krake B")
        elif "Krake C zaključen." in self.history:
            self.open_branches.append("Krake D")
        self.history.clear()
        print("Prehod v naslednjo fazo!")

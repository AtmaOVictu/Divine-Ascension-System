class TaskManager:
    """Manage open and closed branches while tracking history."""

    def __init__(self):
        self.history = []
        self.open_branches = []
        self.closed_branches = []

    def add_open_branch(self, branch: str) -> None:
        """Add a new open branch."""
        self.open_branches.append(branch)

    def close_branch(self, branch: str) -> None:
        """Close a branch and record it in history."""
        if branch in self.open_branches:
            self.open_branches.remove(branch)
            self.closed_branches.append(branch)
            self.history.append(f"{branch} zaključen.")
            self.check_for_progress()

    def check_for_progress(self) -> None:
        """Advance if there are no open branches left."""
        if len(self.open_branches) == 0:
            self.advance_to_next_stage()

    def advance_to_next_stage(self) -> None:
        """Open the next branch based on recorded history."""
        if any("Krake A" in entry for entry in self.history):
            print("Zgodovina prehodov kaže, da je naslednji korak B.")
            self.open_branches.append("Krake B")
        elif any("Krake C" in entry for entry in self.history):
            print("Zgodovina prehodov kaže, da je naslednji korak D.")
            self.open_branches.append("Krake D")
        self.history.clear()
        print("Prehod v naslednjo fazo!")

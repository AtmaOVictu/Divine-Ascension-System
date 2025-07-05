class ErrorManager:
    """Manage errors and store them as potential issues."""

    def __init__(self) -> None:
        self.errors = []
        self.potential_issues = []

    def log_error(self, message: str, error_type: str = "General") -> None:
        """Record an error and save it as a potential issue."""
        error = {"message": message, "type": error_type}
        self.errors.append(error)
        self.potential_issues.append(error)

    def resolve_error(self, message: str) -> bool:
        """Remove an error from potential issues once resolved."""
        for issue in list(self.potential_issues):
            if issue["message"] == message:
                self.potential_issues.remove(issue)
                return True
        return False

    def list_potentials(self):
        return self.potential_issues

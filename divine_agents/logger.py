class SimpleErrorLogger:
    """Minimal logger to track error messages."""

    def __init__(self):
        self.errors = []

    def log_error(self, error_message: str) -> None:
        """Store an error message."""
        self.errors.append(error_message)

    def show_errors(self):
        """Return list of logged errors."""
        return list(self.errors)

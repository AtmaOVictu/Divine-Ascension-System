class InvalidCapacitor:
    """Validate operations based on the agent's state."""

    INVALID_STATES = {"Ego", "Conflicted", "Stagnant"}

    def __init__(self):
        self.invalid_operations = []
        self.valid_operations = []

    def validate_operation(self, operation: str, state: str) -> bool:
        """Check if the operation is allowed in the current state."""
        if state in self.INVALID_STATES:
            self.invalid_operations.append(operation)
            return False
        self.valid_operations.append(operation)
        return True

    def report(self) -> str:
        return (
            f"Invalid: {self.invalid_operations}, "
            f"Valid: {self.valid_operations}"
        )

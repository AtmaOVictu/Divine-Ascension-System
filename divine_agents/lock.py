class Lock:
    """Represents a lock based on a value threshold."""

    def __init__(self, name: str, condition_type: str, threshold: float):
        self.name = name
        self.condition_type = condition_type
        self.threshold = threshold
        self.locked = True

    def attempt_unlock(self, value: float) -> bool:
        """Unlock if the provided value exceeds the threshold."""
        if value > self.threshold:
            self.locked = False
        return not self.locked

    def is_locked(self) -> bool:
        """Return True if the lock is still locked."""
        return self.locked

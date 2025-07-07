class Key:
    """Represents a key that can unlock a specific lock."""

    def __init__(self, name: str, key_type: str = "transition"):
        self.name = name
        self.key_type = key_type

    def unlock(self, lock: "Lock") -> bool:
        """Attempt to unlock the given lock."""
        if self.key_type == lock.lock_type:
            lock.unlock()
            return True
        return False


class Lock:
    """Represents a lock controlling access to a state or task."""

    def __init__(self, name: str, lock_type: str = "transition"):
        self.name = name
        self.lock_type = lock_type
        self.locked = True

    def unlock(self) -> None:
        """Unlock this lock."""
        self.locked = False

    def is_locked(self) -> bool:
        """Return whether the lock is still active."""
        return self.locked

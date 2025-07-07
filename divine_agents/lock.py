class Lock:
    """Represents a lock preventing state transitions until unlocked."""

    def __init__(self, name: str, lock_type: str = "state", condition: str = "emotion"):
        self.name = name
        self.lock_type = lock_type
        self.condition = condition
        self.locked = True

    def unlock(self) -> str:
        """Unlock this lock."""
        self.locked = False
        return f"{self.name} unlocked"

    def is_locked(self) -> bool:
        """Return True if the lock is still active."""
        return self.locked


class Key:
    """Represents a key capable of unlocking locks."""

    def __init__(self, name: str, key_type: str = "emotion"):
        self.name = name
        self.key_type = key_type

    def use(self, lock: Lock) -> str:
        """Attempt to unlock a lock if key matches the condition."""
        if self.key_type == lock.condition:
            return lock.unlock()
        return f"{self.name} cannot unlock {lock.name}"

class Lock:
    """Represents a lock preventing state transitions until unlocked."""

    def __init__(self, name: str, condition: str = "emotion"):
        self.name = name
        self.condition = condition
        self.locked = True

    def unlock(self) -> None:
        """Unlock the lock."""
        self.locked = False

    def is_locked(self) -> bool:
        """Return True if still locked."""
        return self.locked


class Key:
    """Represents a key used to unlock a lock based on condition."""

    def __init__(self, name: str, key_type: str = "emotion"):
        self.name = name
        self.key_type = key_type

    def use(self, lock: Lock) -> bool:
        """Attempt to unlock the provided lock. Return True if unlocked."""
        if self.key_type == lock.condition:
            lock.unlock()
            return True
        return False

class Key:
    """Represents a key that can unlock a specific type of lock."""

    def __init__(self, name: str, key_type: str = "basic"):
        self.name = name
        self.key_type = key_type

    def unlock(self, lock: 'Lock') -> bool:
        """Attempt to unlock a lock using this key."""
        if self.key_type == lock.lock_type and lock.locked:
            lock.unlock()
            return True
        return False


class Lock:
    """Represents a lock that guards access to a state or task."""

    def __init__(self, name: str, lock_type: str = "basic"):
        self.name = name
        self.lock_type = lock_type
        self.locked = True

    def unlock(self) -> None:
        """Unlock this lock."""
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked

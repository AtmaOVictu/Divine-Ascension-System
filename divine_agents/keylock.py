class Key:
    """Represents a key capable of unlocking a compatible lock."""

    def __init__(self, name: str, key_type: str = "basic") -> None:
        self.name = name
        self.key_type = key_type

    def unlock(self, lock: "Lock") -> bool:
        """Attempt to unlock the provided lock."""
        if self.key_type == lock.lock_type and lock.locked:
            lock.unlock()
            return True
        return False


class Lock:
    """Represents a lock controlling access to transitions or tasks."""

    def __init__(self, name: str, lock_type: str = "basic") -> None:
        self.name = name
        self.lock_type = lock_type
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked
